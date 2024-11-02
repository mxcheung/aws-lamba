import boto3
import json
import base64

def lambda_handler(event, context):
    # Retrieve file and headers from the incoming event
    file_content = event.get("file_content")  # Assuming base64 encoded string
    headers = event.get("headers", {})  # Assuming headers is a dictionary

    # Create the payload for LambdaFunction2
    payload = {
        "file_content": file_content,
        "headers": headers
    }

    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName='LambdaFunction2',
        InvocationType='RequestResponse',  # Use 'Event' for asynchronous invocation
        Payload=json.dumps(payload)
    )

    # Read the response from LambdaFunction2
    response_payload = json.loads(response['Payload'].read().decode('utf-8'))
    return {
        "statusCode": 200,
        "body": response_payload
    }
