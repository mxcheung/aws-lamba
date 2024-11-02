#!/bin/bash

export S3_BUCKET_NAME="S3TriggerLambdaBucketQaisar"
export LAMBDA_FUNCTION_NAME="S3TriggerLambda"
export LAMBDA_ROLE_NAME="LambdaS3ExecutionRole"

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

aws lambda add-permission \
  --function-name $LAMBDA_FUNCTION_NAME \
  --principal s3.amazonaws.com \
  --statement-id AllowS3Invoke \
  --action "lambda:InvokeFunction" \
  --source-arn arn:aws:s3:::$S3_BUCKET_NAME \
  --source-account $AWS_ACCOUNT_ID


aws lambda add-permission --function-name LambdaFunction2 \
    --statement-id AllowInvokeFromLambdaFunction1 \
    --action lambda:InvokeFunction \
    --principal lambda.amazonaws.com \
    --source-arn arn:aws:lambda:<region>:<your_account_id>:function:LambdaFunction1
