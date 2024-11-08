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

aws lambda add-permission --function-name $LAMBDA_FUNCTION_2_NAME \
    --statement-id AllowInvokeFromLambdaFunction1 \
    --action lambda:InvokeFunction \
    --principal lambda.amazonaws.com \
    --source-arn arn:aws:lambda:$REGION:$AWS_ACCOUNT_ID:function:$LAMBDA_FUNCTION_1_NAME

