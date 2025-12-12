
```
aws lambda update-function-code --function-name MyLambdaFunction --zip-file fileb://my_lambda_function.zip --publish
```

If you are uploading a big .zip (50–200 MB), some networks cut the TLS connection.

✔️ Fix: Use S3 for uploads
```
aws s3 cp fn.zip s3://mybucket/lambda/
aws lambda update-function-code \
  --function-name fn \
  --s3-bucket mybucket \
  --s3-key lambda/fn.zip

```

```
BUCKET_NAME="my-lambda-upload-bucket-12345"
REGION="ap-southeast-2"

aws s3api create-bucket \
  --bucket $BUCKET_NAME \
  --region $REGION \
  --create-bucket-configuration LocationConstraint=$REGION
```

```
ROLE_ARN="arn:aws:iam::123456789012:role/MyCodeBuildRole"
PREFIX="lambda/*"
```

```
cat > bucket-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "$ROLE_ARN"
      },
      "Action": [
        "s3:PutObject",
        "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::$BUCKET_NAME/$PREFIX"
    }
  ]
}
EOF
```

Apply the policy to the bucket
```
aws s3api put-bucket-policy \
  --bucket $BUCKET_NAME \
  --policy file://bucket-policy.json
```

