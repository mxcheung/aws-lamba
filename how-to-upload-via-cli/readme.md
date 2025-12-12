
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
