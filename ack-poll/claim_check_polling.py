import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract claim check ID from the incoming event
    claim_check_id = event['claim_check_id']
    bucket_name = 'your-s3-bucket-name'
    object_key = f'uploads/{claim_check_id}/file.txt'

    try:
        # Check if the file exists in S3
        s3.head_object(Bucket=bucket_name, Key=object_key)
        return {
            'claim_check_id': claim_check_id,
            'status': 'completed',
            'message': 'File upload successful.'
        }
    except s3.exceptions.NoSuchKey:
        # File not found, indicating the upload is still in progress
        return {
            'claim_check_id': claim_check_id,
            'status': 'pending',
            'message': 'File upload still in progress. Retry later.'
        }
