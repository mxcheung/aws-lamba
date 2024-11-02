#!/bin/bash


export LAMBDA_FUNCTION_1_NAME="LambdaFunction1"
export LAMBDA_FUNCTION_2_NAME="LambdaFunction2"
export LAMBDA_1_ROLE_NAME="LambdaInvokeRole1"
export LAMBDA_2_ROLE_NAME="LambdaInvokeRole2"


aws lambda wait function-active --function-name $LAMBDA_FUNCTION_1_NAME
echo " $LAMBDA_FUNCTION_1_NAME is active."

aws lambda wait function-active --function-name $LAMBDA_FUNCTION_2_NAME
echo " $LAMBDA_FUNCTION_2_NAME is active."


# Set variables
REGION="us-east-1"                                  # Replace with your desired AWS region
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

# Check if AWS_ACCOUNT_ID was retrieved successfully
if [[ -z "$AWS_ACCOUNT_ID" ]]; then
    echo "Error: Unable to retrieve AWS account ID."
    exit 1
fi

chmod +x generate_invoke_policy.sh

./generate_invoke_policy.sh

aws iam put-role-policy \
    --role-name LambdaInvokeRole1 \
    --policy-name InvokeLambdaFunction2Policy \
    --policy-document file://invoke_policy.json


aws lambda add-permission --function-name $LAMBDA_FUNCTION_2_NAME \
    --statement-id AllowInvokeFromLambdaFunction1 \
    --action lambda:InvokeFunction \
    --principal lambda.amazonaws.com \
    --source-arn arn:aws:lambda:$REGION:$AWS_ACCOUNT_ID:function:$LAMBDA_FUNCTION_1_NAME


# Function to wait for the policy to be updated
wait_for_policy_update() {
    local retries=5
    local wait_time=5  # Wait time between retries in seconds
    local statement_id="AllowInvokeFromLambdaFunction1"

    for ((i=0; i<retries; i++)); do
        POLICY=$(aws lambda get-policy --function-name $LAMBDA_FUNCTION_2_NAME --query 'Policy' --output text 2>/dev/null)

        if [[ "$POLICY" == *"$statement_id"* ]]; then
            echo "Permission successfully added."
            return 0
        fi

        echo "Waiting for permissions to be added... (Attempt $((i + 1)))"
        sleep $wait_time
    done

    echo "Failed to add permission after $retries attempts."
    return 1
}

# Wait for the permission to be updated
wait_for_policy_update

# Check if the permission was successfully added
if [[ $? -ne 0 ]]; then
    exit 1  # Exit if the permission was not added
fi

    
