import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as s3notifications from 'aws-cdk-lib/aws-s3-notifications';

export class S3LambdaTriggerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Assuming the S3 bucket and Lambda function already exist.
    const bucket = s3.Bucket.fromBucketName(this, 'ExistingBucket', 'my-existing-bucket-name');
    const func = lambda.Function.fromFunctionArn(this, 'ExistingLambdaFunction', 'arn:aws:lambda:region:account-id:function:my-function-name');

    // Set up the S3 trigger for the Lambda function on object creation events
    bucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3notifications.LambdaDestination(func),
      { prefix: 'uploads/', suffix: '.csv' } // Optional: filters to trigger only on specific files
    );

    // Grant the bucket permissions to invoke the Lambda function
    bucket.grantRead(func);
  }
}
