#!/bin/bash

export LAMBDA_FUNCTION_NAME="LambdaFunction1"
export LAMBDA_ROLE_NAME="LambdaInvokeRole1"
export LAMBDA_FUNCTION_2_NAME="LambdaFunction2"

# Variables
REGION="us-east-1"                                  # Replace with your AWS region

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

zip function.zip lambda_function.py

# Wait for the IAM role to be created
aws iam wait role-exists --role-name $LAMBDA_ROLE_NAME

export LAMBDA_ROLE_ARN=$(aws iam get-role --role-name $LAMBDA_ROLE_NAME --query 'Role.Arn' --output text)

aws lambda create-function \
    --function-name $LAMBDA_FUNCTION_NAME \
    --zip-file fileb://function.zip \
    --handler lambda_function.lambda_handler \
    --runtime python3.9 \
    --role $LAMBDA_ROLE_ARN 
    --environment Variables="{LAMBDA_FUNCTION_2_NAME=$LAMBDA_FUNCTION_2_NAME}")

