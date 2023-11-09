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

aws lambda invoke --function-name YourFunctionName --payload file://payload.json --cli-binary-format raw-in-base64-out --log-type Tail --query 'LogResult' --output text | base64 -d

```

## Bash script
```
#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <lambda_name> <payload_file>"
    exit 1
fi

lambda_name=$1
payload_file=$2


# Print the Lambda function name
echo "Invoking Lambda function: $lambda_name"

# Invoke the Lambda function
aws lambda invoke --function-name "$lambda_name" --payload "file://$payload_file" --cli-binary-format raw-in-base64-out --log-type Tail --query 'LogResult' --output text | base64 --decode
```
