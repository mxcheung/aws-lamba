import * as cdk from 'aws-cdk-lib';
import { Stack, StackProps } from 'aws-cdk-lib';
import { LambdaFunction } from 'aws-cdk-lib/aws-events-targets';
import { Rule, EventPattern } from 'aws-cdk-lib/aws-events';
import { Function, Runtime, Code } from 'aws-cdk-lib/aws-lambda';
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class S3EventBridgeLambdaStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Create the S3 bucket
    const bucket = new Bucket(this, 'MyBucket');

    // Create the Lambda function within a VPC (assume VPC configuration)
    const lambdaFunction = new Function(this, 'MyFunction', {
      runtime: Runtime.NODEJS_18_X,
      code: Code.fromAsset('lambda'), // specify your Lambda code path
      handler: 'index.handler',
      // ... other function configurations, such as VPC and security groups
    });

    // Define EventBridge rule for S3 event notifications
    const rule = new Rule(this, 'S3EventBridgeRule', {
      eventPattern: {
        source: ['aws.s3'],
        detailType: ['Object Created'],
        resources: [bucket.bucketArn],
      },
    });

    // Set the Lambda function as the target for the rule
    rule.addTarget(new LambdaFunction(lambdaFunction));

    // Grant necessary permissions
    bucket.grantRead(lambdaFunction);
    lambdaFunction.addPermission('AllowEventBridgeInvoke', {
      principal: new cdk.aws_iam.ServicePrincipal('events.amazonaws.com'),
      sourceArn: rule.ruleArn,
    });
  }
}
