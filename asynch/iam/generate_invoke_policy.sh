#!/bin/bash

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
