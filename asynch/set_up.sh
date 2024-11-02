#!/bin/bash

cd /home/ec2-user/aws-s3/presign_url/user_credentials
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/iam
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/s3
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/lambda
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/lambda_presign_url
. ./set_up.sh


cd /home/ec2-user/aws-s3/presign_url/lambda_permission
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/s3_notification
. ./set_up.sh

cd /home/ec2-user/aws-s3/presign_url/s3_test_upload
. ./set_up.sh
