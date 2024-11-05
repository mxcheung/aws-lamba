# import
from utilities.lambda_aspects import (
    FunctionInVpc
)
 
# In code
# Create a list with private subnets to be used in the aspect to make all lambda's deployed in a VPC
private_subnet1_id_token = ssm.StringParameter.value_for_string_parameter(self, '/gts-aacb/vpc/private-subnet-1-id')
private_subnet2_id_token = ssm.StringParameter.value_for_string_parameter(self, '/gts-aacb/vpc/private-subnet-2-id')
private_subnet3_id_token = ssm.StringParameter.value_for_string_parameter(self, '/gts-aacb/vpc/private-subnet-3-id')
private_subnet_ids=[private_subnet1_id_token, private_subnet2_id_token, private_subnet3_id_token]
 
# Create a lambda Security Group where all lambdas are in
lambdaSG = ec2.SecurityGroup(
  self, 'LambdaSG',
  vpc=vpc.vpc,
  description="Lambda security group",
  allow_all_outbound=True
)
 
# End statement
core.Aspects.of(self).add(FunctionInVPC(private_subnets=private_subnet_ids, security_group_id=lambdaSG.security_group_id))
