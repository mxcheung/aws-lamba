import boto3  # AWS SDK for Python
import json
import logging
import urllib.request

s3 = boto3.client("s3")

# Constants
EVENTBRIDGE_CONFIGURATION = 'EventBridgeConfiguration'
CONFIGURATION_TYPES = ["TopicConfigurations", "QueueConfigurations", "LambdaFunctionConfigurations"]

# Main handler function
def handler(event: dict, context):
    response_status = "SUCCESS"
    error_message = ""
    
    try:
        # Extract resource properties from the CloudFormation event
        props = event["ResourceProperties"]
        bucket = props["BucketName"]
        notification_configuration = props["NotificationConfiguration"]
        request_type = event["RequestType"]
        managed = props.get('Managed', 'true').lower() == 'true'
        stack_id = event['StackId']
        
        # Handle managed vs unmanaged configurations
        if managed:
            config = handle_managed(request_type, notification_configuration)
        else:
            config = handle_unmanaged(bucket, stack_id, request_type, notification_configuration)
        
        # Update bucket notification configuration
        put_bucket_notification_configuration(bucket, config)
        
    except Exception as e:
        logging.exception("Failed to put bucket notification configuration")
        response_status = "FAILED"
        error_message = f"Error: {str(e)}. "
        
    finally:
        # Send response back to CloudFormation
        submit_response(event, context, response_status, error_message)

# Managed request type handler
def handle_managed(request_type, notification_configuration):
    if request_type == 'Delete':
        return {}  # Clear notifications on delete
    return notification_configuration

# Unmanaged request type handler
def handle_unmanaged(bucket, stack_id, request_type, notification_configuration):
    external_notifications = find_external_notifications(bucket, stack_id)

    if request_type == 'Delete':
        return external_notifications

    # Function to assign unique IDs to each notification
    def with_id(notification):
        notification['Id'] = f"{stack_id}-{hash(json.dumps(notification, sort_keys=True))}"
        return notification

    # Merge incoming notifications with external ones
    notifications = {}
    for t in CONFIGURATION_TYPES:
        external = external_notifications.get(t, [])
        incoming = [with_id(n) for n in notification_configuration.get(t, [])]
        notifications[t] = external + incoming

    # Handle EventBridge configuration separately
    if EVENTBRIDGE_CONFIGURATION in notification_configuration:
        notifications[EVENTBRIDGE_CONFIGURATION] = notification_configuration[EVENTBRIDGE_CONFIGURATION]
    elif EVENTBRIDGE_CONFIGURATION in external_notifications:
        notifications[EVENTBRIDGE_CONFIGURATION] = external_notifications[EVENTBRIDGE_CONFIGURATION]

    return notifications

# Retrieve notifications not managed by the stack
def find_external_notifications(bucket, stack_id):
    existing_notifications = get_bucket_notification_configuration(bucket)
    external_notifications = {}
    
    for t in CONFIGURATION_TYPES:
        external_notifications[t] = [
            n for n in existing_notifications.get(t, []) if not n['Id'].startswith(f"{stack_id}-")
        ]

    if EVENTBRIDGE_CONFIGURATION in existing_notifications:
        external_notifications[EVENTBRIDGE_CONFIGURATION] = existing_notifications[EVENTBRIDGE_CONFIGURATION]

    return external_notifications

# Get the current bucket notification configuration
def get_bucket_notification_configuration(bucket):
    return s3.get_bucket_notification_configuration(Bucket=bucket)

# Set the bucket notification configuration
def put_bucket_notification_configuration(bucket, notification_configuration):
    s3.put_bucket_notification_configuration(Bucket=bucket, NotificationConfiguration=notification_configuration)

# Function to send the response back to CloudFormation
def submit_response(event: dict, context, response_status: str, error_message: str):
    response_body = json.dumps({
        "Status": response_status,
        "Reason": f"{error_message} See the details in CloudWatch Log Stream: {context.log_stream_name}",
        "PhysicalResourceId": event.get("PhysicalResourceId") or event["LogicalResourceId"],
        "StackId": event["StackId"],
        "RequestId": event["RequestId"],
        "LogicalResourceId": event["LogicalResourceId"],
        "NoEcho": False,
    }).encode("utf-8")
    
    headers = {"content-type": "", "content-length": str(len(response_body))}
    try:
        req = urllib.request.Request(url=event["ResponseURL"], headers=headers, data=response_body, method="PUT")
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
        print("Status code:", response.reason)
    except Exception as e:
        print("Failed to send response to CloudFormation:", str(e))
