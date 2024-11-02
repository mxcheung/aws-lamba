import json
import boto3
import os

lambda_client = boto3.client("lambda")

def lambda_handler(event, context):
    # Prepare the payload for LambdaFunction2
    payload = {
        "file_content": event.get("file_content"),
        "headers": event.get("headers")
    }
    
    # Invoke LambdaFunction2 asynchronously
    response = lambda_client.invoke(
        FunctionName=os.environ["LAMBDA_FUNCTION_2_NAME"],
        InvocationType="Event",  # Asynchronous invocation
        Payload=json.dumps(payload)
    )
    
    # Immediately return response from LambdaFunction1
    return {
        "statusCode": 202,
        "body": json.dumps({
            "message": "LambdaFunction2 invocation triggered asynchronously",
            "LambdaFunction2RequestId": response['ResponseMetadata']['RequestId']
        })
    }
