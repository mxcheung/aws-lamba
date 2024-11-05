import * as cdk from 'aws-cdk-lib';
import { aws_lambda as lambda, aws_iam as iam } from 'aws-cdk-lib';

export class FunctionInVPC implements cdk.IAspect {
  private readonly privateSubnets: string[];
  private readonly securityGroupId: string;

  constructor(privateSubnets: string[], securityGroupId: string) {
    this.privateSubnets = privateSubnets;
    this.securityGroupId = securityGroupId;
  }

  public visit(node: cdk.IConstruct): void {
    if (node instanceof iam.Role) {
      const cfnRole = node.node.tryFindChild('Resource') as iam.CfnRole;
      const metadata = cfnRole?.getMetadata('aws:cdk:path');
      
      if (metadata && metadata.includes('BucketNotificationsHandler')) {
        node.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaVPCAccessExecutionRole'));
      }
    }

    if (node instanceof cdk.CfnResource) {
      if (node.cfnResourceType === 'AWS::Lambda::Function') {
        node.addPropertyOverride('VpcConfig.SecurityGroupIds', [this.securityGroupId]);
        node.addPropertyOverride('VpcConfig.SubnetIds', this.privateSubnets);
      }
    }
  }
}
