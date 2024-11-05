import jsii
from aws_cdk import (
    aws_lambda as awslambda,
    aws_iam as iam,
    core
)
"""
This is a lambda aspect to make Lambda used in CDK compliant. It makes sure that the created Lambda helper functions,
such as used by custom resources, are deployed inside your VPC
"""
@jsii.implements(core.IAspect)
# Aspect to run Lambda function inside VPC by overriding CloudFormation property
class FunctionInVPC:
    def __init__(self, private_subnets: str, security_group_id: str) -> None:
        # retrieve the private subnets and security group to use
        self.private_subnets = private_subnets
        self.security_group_id = security_group_id
    def visit(self, construct: core.IConstruct) -> None:
        if isinstance(construct, iam.Role):
            # Add the managed policy AWSLambdaVPCAccessExecutionRole to the bucketNotificationHandler function so it is able to create an ENI
            cfn_role = construct.node.find_child('Resource')
            metadata = cfn_role.get_metadata('aws:cdk:path')
            if 'BucketNotificationsHandler' in metadata:
                construct.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaVPCAccessExecutionRole')),
 
        if isinstance(construct, core.CfnResource):
            # add the Security group and subnet to the properties of the lambda function
            if construct.cfn_resource_type in ['AWS::Lambda::Function']:
                construct.add_property_override('VpcConfig.SecurityGroupIds',[self.security_group_id]),
                construct.add_property_override('VpcConfig.SubnetIds',self.private_subnets),
