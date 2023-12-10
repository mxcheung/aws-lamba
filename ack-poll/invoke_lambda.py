import boto3

def lambda_handler(event, context):
    # Replace 'YourFunctionName' with the name of the Lambda function you want to invoke
    function_name = 'YourFunctionName'
    
    # Replace 'your-region' with the AWS region where the target Lambda function is deployed
    region = 'your-region'

    # Create a Boto3 Lambda client
    lambda_client = boto3.client('lambda', region_name=region)

    # Prepare the payload to send to the target Lambda function
    payload = {
        'key1': 'value1',
        'key2': 'value2'
        # Add any other input parameters your Lambda function expects
    }

    # Invoke the target Lambda function
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',  # Use 'Event' for asynchronous invocation
        Payload=json.dumps(payload)
    )

    # Process the response if needed
    result = json.loads(response['Payload'].read())
    print(result)
    
    # Handle other logic based on the response

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function invoked successfully!')
    }
