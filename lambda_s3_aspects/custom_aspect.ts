import * as cdk from 'aws-cdk-lib';
import { Stack, App, Aspects } from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import { IConstruct } from 'constructs';

// Custom aspect to enforce VPC on Lambda functions
class LambdaVpcAspect implements cdk.IAspect {
  private readonly vpc: ec2.Vpc;

  constructor(vpc: ec2.Vpc) {
    this.vpc = vpc;
  }

  visit(node: IConstruct): void {
    if (node instanceof lambda.Function) {
      node.addEnvironment("VPC_ENABLED", "true");
      node.addVpc(this.vpc);  // Attach the VPC configuration to the Lambda
    }
  }
}

class S3LambdaVpcStack extends Stack {
  constructor(scope: App, id: string) {
    super(scope, id);

    // Create a VPC
    const vpc = new ec2.Vpc(this, 'MyVpc', {
      maxAzs: 2,
      natGateways: 1,
    });

    // Create an S3 bucket
    const bucket = new s3.Bucket(this, 'MyBucket');

    // Define the Lambda function
    const myLambda = new lambda.Function(this, 'MyFunction', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('lambda'),
      vpc,  // Directly assign VPC here
    });

    // Grant the Lambda function permission to read from the S3 bucket
    bucket.grantRead(myLambda);

    // Create an S3 event notification to trigger the Lambda function
    bucket.addEventNotification(s3.EventType.OBJECT_CREATED, new s3n.LambdaDestination(myLambda));

    // Apply the Lambda VPC aspect to the stack
    Aspects.of(this).add(new LambdaVpcAspect(vpc));
  }
}

const app = new App();
new S3LambdaVpcStack(app, 'S3LambdaVpcStack');
