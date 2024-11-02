#!/bin/bash


export LAMBDA_FUNCTION_1_NAME="LambdaFunction1"
export LAMBDA_FUNCTION_2_NAME="LambdaFunction2"
export LAMBDA_1_ROLE_NAME="LambdaInvokeRole1"
export LAMBDA_2_ROLE_NAME="LambdaInvokeRole2"

# Set variables
REGION="us-east-1"                                  # Replace with your desired AWS region
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

# Check if AWS_ACCOUNT_ID was retrieved successfully
if [[ -z "$AWS_ACCOUNT_ID" ]]; then
    echo "Error: Unable to retrieve AWS account ID."
    exit 1
fi

# Create the invoke_policy.json with dynamic values
cat <<EOF > invoke_policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:$REGION:$AWS_ACCOUNT_ID:function:LambdaFunction2"
        }
    ]
}
EOF

echo "Policy file 'invoke_policy.json' created successfully with region $REGION and account ID $AWS_ACCOUNT_ID."


aws lambda add-permission --function-name $LAMBDA_FUNCTION_2_NAME \
    --statement-id AllowInvokeFromLambdaFunction1 \
    --action lambda:InvokeFunction \
    --principal lambda.amazonaws.com \
    --source-arn arn:aws:lambda:$REGION:$AWS_ACCOUNT_ID:function:$LAMBDA_FUNCTION_1_NAME
