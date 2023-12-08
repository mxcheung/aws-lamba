import boto3

# Set your AWS credentials
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
region_name = 'your_region'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Specify your S3 bucket and object key (UUID 123)
bucket_name = 'your_bucket_name'
object_key = '123'

# Get the object from S3
try:
    response = s3.get_object(Bucket=bucket_name, Key=object_key)

    # Access the object data
    object_data = response['Body'].read()

    # Do something with the object data (e.g., print it)
    print(object_data.decode('utf-8'))

except Exception as e:
    print(f"Error: {e}")
