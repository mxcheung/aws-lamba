#!/bin/bash

cd /home/ec2-user/aws-s3/presign_url/user_credentials
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/iam
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/lambda_1
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/lambda_2
. ./set_up.sh


