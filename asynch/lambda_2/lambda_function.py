import json

def lambda_handler(event, context):
    # Example processing logic
    message_from_lambda1 = event.get("message", "No message received")
    print(f"Received message: {message_from_lambda1}")

    # You can add additional logic here as needed
    return {
        "statusCode": 200,
        "body": f"LambdaFunction2 received: {message_from_lambda1}"
    }
