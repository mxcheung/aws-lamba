import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import { Role, ServicePrincipal, PolicyStatement } from 'aws-cdk-lib/aws-iam';

export class S3LambdaTriggerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Import the existing Lambda function by ARN
    const lambdaFunction = lambda.Function.fromFunctionArn(this, 'ExistingLambda', 'arn:aws:lambda:your-region:your-account-id:function:your-lambda-function-name');

    // Import the existing S3 bucket
    const bucket = s3.Bucket.fromBucketName(this, 'ExistingBucket', 'your-bucket-name');

    // Grant Lambda function permissions to read from the bucket
    bucket.grantRead(lambdaFunction);

    // Add the S3 event notification to trigger the Lambda function on object creation
    bucket.addEventNotification(s3.EventType.OBJECT_CREATED_PUT, new s3n.LambdaDestination(lambdaFunction));
  }
}
