import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as lambdaEventSources from 'aws-cdk-lib/aws-lambda-event-sources';

export class S3LambdaEventSourceStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Import the existing S3 bucket and Lambda function
    const bucket = s3.Bucket.fromBucketName(this, 'ExistingBucket', 'my-existing-bucket-name');
    const func = lambda.Function.fromFunctionArn(this, 'ExistingLambdaFunction', 'arn:aws:lambda:region:account-id:function:my-function-name');

    // Define the S3 event source
    const s3EventSource = new lambdaEventSources.S3EventSource(bucket, {
      events: [s3.EventType.OBJECT_CREATED],
      filters: [{ prefix: 'uploads/', suffix: '.csv' }], // Optional: filters to trigger on specific files
    });

    // Add the S3 event source to the Lambda function
    func.addEventSource(s3EventSource);
  }
}
