#!/bin/bash

export LAMBDA_FUNCTION_NAME="S3TriggerLambda"
export LAMBDA_ROLE_NAME="LambdaS3ExecutionRole"

aws iam create-role \
    --role-name  $LAMBDA_ROLE_NAME \
    --assume-role-policy-document file://trust-policy.json

# Wait for the IAM role to be created
aws iam wait role-exists --role-name $LAMBDA_ROLE_NAME


aws iam attach-role-policy --role-name $LAMBDA_ROLE_NAME --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam attach-role-policy --role-name $LAMBDA_ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
    
