import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime

# Replace 'your_table_name' with your DynamoDB table name
table_name = 'your_table_name'
status_value = 'QUEUE'

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# Query the DynamoDB table
response = table.query(
    IndexName='status-insert_timestamp-index',  # Replace with your actual index name
    KeyConditionExpression=Key('status').eq(status_value),
    ScanIndexForward=True,  # Ascending order for insert_timestamp
    Limit=1
)

# Check if there are items matching the condition
if response.get('Items'):
    # Get the first item with the earliest insert_timestamp
    first_record = min(response['Items'], key=lambda x: x['insert_timestamp'])
    
    # Print or process the first record
    print("First Record:", first_record)
else:
    print("No records with status '{}' found.".format(status_value))
