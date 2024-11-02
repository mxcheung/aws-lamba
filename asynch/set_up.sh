#!/bin/bash

cd /home/ec2-user/aws-lamba/asynch/user_credentials
. ./set_up.sh

cd /home/ec2-user/aws-lamba/asynch/iam
. ./set_up.sh

cd /home/ec2-user/aws-lamba/asynch/lambda_1
. ./set_up.sh

cd /home/ec2-user/aws-lamba/asynch/lambda_2
. ./set_up.sh

cd /home/ec2-user/aws-lamba/asynch/test_lambda
. ./set_up.sh
