#!/bin/bash

export LAMBDA_FUNCTION_NAME="S3PresignURLLambda"
export LAMBDA_ROLE_NAME="LambdaS3ExecutionRole"

# Variables
BASE_BUCKET_NAME="s3triggerlambdabucketqaisar"
REGION="us-east-1"                                  # Replace with your AWS region

# Get the existing S3 bucket name based on the base name
export S3_BUCKET_NAME=$(aws s3api list-buckets --query "Buckets[?starts_with(Name, \`${BASE_BUCKET_NAME}\`)].Name" --output text)



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
    --role $LAMBDA_ROLE_ARN \
    --environment Variables="{BUCKET_NAME=$S3_BUCKET_NAME}"
