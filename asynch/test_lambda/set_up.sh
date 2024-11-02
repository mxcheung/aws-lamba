#!/bin/bash

# Set variables


REGION="us-east-1"                                  # Replace with your AWS region

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)


LAMBDA_FUNCTION_NAME="LambdaFunction1"
FILE_PATH="sample.txt"  # Path to your test file
OUTPUT_FILE="output.json"
TEST_PAYLOAD="test_event.json"

# Check if the file exists
if [[ ! -f "$FILE_PATH" ]]; then
    echo "Error: File '$FILE_PATH' not found!"
    exit 1
fi

# Step 1: Base64 encode the file content, removing any newline characters
echo "Encoding file: $FILE_PATH"
FILE_CONTENT_BASE64=$(base64 "$FILE_PATH" | tr -d '\n')

# Step 2: Create a test payload with headers
echo "Creating test payload..."
cat <<EOF > $TEST_PAYLOAD
{
    "file_content": "$FILE_CONTENT_BASE64",
    "headers": {
        "Content-Type": "text/plain",
        "Custom-Header": "TestHeaderValue"
    }
}
EOF

# Step 3: Invoke LambdaFunction1 with the test payload
echo "Invoking LambdaFunction1..."
aws lambda invoke \
    --function-name "$LAMBDA_FUNCTION_NAME" \
    --payload file://$TEST_PAYLOAD \
    --region $REGION \
    $OUTPUT_FILE

# Step 4: Display the output from LambdaFunction2
echo "Lambda invocation complete. Output:"
cat $OUTPUT_FILE
echo

# Optional: Clean up the test files
# rm $TEST_PAYLOAD $OUTPUT_FILE
