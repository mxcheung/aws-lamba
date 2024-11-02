
```
{
    "Statement": "{\"Sid\":\"AllowS3Invoke\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"s3.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-east-1:058264537146:function:S3TriggerLambda\",\"Condition\":{\"StringEquals\":{\"AWS:SourceAccount\":\"058264537146\"},\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:s3:::S3TriggerLambdaBucketQaisar\"}}}"
```
