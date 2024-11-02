#!/bin/bash


export LAMBDA_FUNCTION_1_NAME="LambdaFunction1"
export LAMBDA_FUNCTION_2_NAME="LambdaFunction2"
export LAMBDA_1_ROLE_NAME="LambdaInvokeRole1"
export LAMBDA_2_ROLE_NAME="LambdaInvokeRole2"

REGION="us-east-1"                                  # Replace with your AWS region


AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)


aws lambda add-permission --function-name $LAMBDA_FUNCTION_2_NAME \
    --statement-id AllowInvokeFromLambdaFunction1 \
    --action lambda:InvokeFunction \
    --principal lambda.amazonaws.com \
    --source-arn arn:aws:lambda:$REGION:$AWS_ACCOUNT_ID:function:$LAMBDA_FUNCTION_1_NAME
