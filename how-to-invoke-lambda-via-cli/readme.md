# invoke lambda

```
aws lambda invoke --function-name YourFunctionName --payload '{"key1":"value1", "key2":"value2"}' output.txt
```

## Display results
```
aws lambda invoke --function-name YourFunctionName --payload '{"key1":"value1", "key2":"value2"}' --cli-binary-format raw-in-base64-out --log-type Tail --query 'LogResult' --output text | base64 -d
```

## Invoke with file payload
```
aws lambda invoke --function-name YourFunctionName --payload file://path/to/your/payload.json --cli-binary-format raw-in-base64-out --log-type Tail --query 'LogResult' --output text | base64 -d
```
