#!/bin/bash

export LAMBDA_FUNCTION_1_NAME="LambdaFunction1"
export LAMBDA_FUNCTION_2_NAME="LambdaFunction2"
export LAMBDA_1_ROLE_NAME="LambdaInvokeRole1"
export LAMBDA_2_ROLE_NAME="LambdaInvokeRole2"

aws iam create-role \
    --role-name  $LAMBDA_1_ROLE_NAME \
    --assume-role-policy-document file://trust-policy.json

aws iam create-role \
    --role-name  $LAMBDA_2_ROLE_NAME \
    --assume-role-policy-document file://trust-policy.json
    
# Wait for the IAM role to be created
aws iam wait role-exists --role-name $LAMBDA_1_ROLE_NAME
aws iam wait role-exists --role-name $LAMBDA_2_ROLE_NAME


aws iam attach-role-policy --role-name $LAMBDA_1_ROLE_NAME --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam attach-role-policy --role-name $LAMBDA_2_ROLE_NAME --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole


chmod +x generate_invoke_policy.sh

./generate_invoke_policy.sh

aws iam put-role-policy \
    --role-name LambdaInvokeRole1 \
    --policy-name InvokeLambdaFunction2Policy \
    --policy-document file://invoke_policy.json

    
