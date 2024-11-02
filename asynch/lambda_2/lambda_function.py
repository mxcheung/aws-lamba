import json
import base64

def lambda_handler(event, context):
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
