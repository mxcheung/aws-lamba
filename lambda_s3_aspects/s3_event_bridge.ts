import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';

export class S3LambdaEventBridgeStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Import existing S3 bucket and Lambda function
    const bucket = s3.Bucket.fromBucketName(this, 'ExistingBucket', 'my-existing-bucket-name');
    const func = lambda.Function.fromFunctionArn(this, 'ExistingLambdaFunction', 'arn:aws:lambda:region:account-id:function:my-function-name');

    // Enable EventBridge notifications for the S3 bucket
    bucket.addEventNotification(s3.EventType.OBJECT_CREATED, new s3.EventBridgeDestination());

    // Create an EventBridge rule to trigger the Lambda on bucket notifications
    const rule = new events.Rule(this, 'S3EventRule', {
      eventPattern: {
        source: ['aws.s3'],
        detailType: ['Object Created'],
        detail: {
          bucket: {
            name: [bucket.bucketName],
          },
        },
      },
    });

    // Set the Lambda function as the target of the rule
