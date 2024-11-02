import json
import base64
import time
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    start_time = time.time()
    total_duration = 60  # Duration in seconds
    interval = 5         # Interval in seconds for each log entry
    
    # Loop for 60 seconds
    while time.time() - start_time < total_duration:
        # Log a message
        logger.info("LambdaFunction2 is running. Time elapsed: %s seconds", int(time.time() - start_time))
        
        # Wait for the next interval
        time.sleep(interval)
    
    # Final log to indicate completion
    logger.info("LambdaFunction2 completed after %s seconds", total_duration)

    
    # Retrieve file content and headers from the payload
    file_content_base64 = event.get("file_content")
    headers = event.get("headers", {})

    # Decode the file content
    if file_content_base64:
        file_content = base64.b64decode(file_content_base64).decode('utf-8')
    else:
        file_content = "No file content provided"

    # Log or process headers as needed
    print(f"Received headers: {headers}")
    print(f"Received file content: {file_content}")

    # Example processing logic
    result = {
        "message": "File and headers processed successfully",
        "file_summary": f"File content starts with: {file_content[:100]}"  # Truncate for summary
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
