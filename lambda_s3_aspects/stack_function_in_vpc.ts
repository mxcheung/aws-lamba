import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ssm from 'aws-cdk-lib/aws-ssm';
import * as core from 'aws-cdk-lib';
import { FunctionInVpc } from './utilities/lambda_aspects';

// Create a list with private subnets to be used in the aspect to make all lambdas deployed in a VPC
const privateSubnet1IdToken = ssm.StringParameter.valueForStringParameter(this, '/gts-aacb/vpc/private-subnet-1-id');
const privateSubnet2IdToken = ssm.StringParameter.valueForStringParameter(this, '/gts-aacb/vpc/private-subnet-2-id');
const privateSubnet3IdToken = ssm.StringParameter.valueForStringParameter(this, '/gts-aacb/vpc/private-subnet-3-id');
const privateSubnetIds = [privateSubnet1IdToken, privateSubnet2IdToken, privateSubnet3IdToken];

// Create a Lambda Security Group where all Lambdas are in
const lambdaSG = new ec2.SecurityGroup(this, 'LambdaSG', {
  vpc: vpc,
  description: 'Lambda security group',
  allowAllOutbound: true,
});

// Add the aspect to make all Lambdas in the stack use the specified VPC and security group
core.Aspects.of(this).add(new FunctionInVpc({
  privateSubnets: privateSubnetIds,
  securityGroupId: lambdaSG.securityGroupId,
}));
