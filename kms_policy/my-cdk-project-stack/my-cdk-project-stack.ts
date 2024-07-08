import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import * as secretsmanager from '@aws-cdk/aws-secretsmanager';
import * as iam from '@aws-cdk/aws-iam';
import { Key } from '@aws-cdk/aws-kms';

export class MyStack extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // Define a customer managed key
        const key = new Key(this, 'MyKey', {
            enableKeyRotation: true,
        });

        // Define a secret
        const secret = new secretsmanager.Secret(this, 'MySecret', {
            encryptionKey: key,
            secretName: 'mySecret',
        });

        // Define the Lambda function
        const fn = new lambda.Function(this, 'MyFunction', {
            runtime: lambda.Runtime.NODEJS_14_X,
            code: lambda.Code.fromAsset('lambda'),
            handler: 'handler.handler',
            environment: {
                SECRET_NAME: secret.secretName,
                REGION: this.region,
            },
        });

        // Grant the Lambda function permission to read the secret
        secret.grantRead(fn);

        // Add KMS permissions to the Lambda function
        fn.addToRolePolicy(new iam.PolicyStatement({
            actions: ['kms:Decrypt'],
            resources: [key.keyArn],
        }));
    }
}

const app = new cdk.App();
new MyStack(app, 'MyStack');
