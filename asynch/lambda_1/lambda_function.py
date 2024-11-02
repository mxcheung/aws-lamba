import boto3

def lambda_handler(event, context):
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName='LambdaFunction2',
        InvocationType='RequestResponse',  # Use 'Event' for async invocation
        Payload='{}'
    )
    return response
