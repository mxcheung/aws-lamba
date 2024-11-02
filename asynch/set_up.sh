#!/bin/bash

export USER_HOME="/c/git/aws-lamba/asynch"
export USER_HOME="/home/ec2-user/aws-lamba/asynch"

cd $USER_HOME/user_credentials
. ./set_up.sh

cd $USER_HOME/iam
. ./set_up.sh

cd $USER_HOME/lambda_1
. ./set_up.sh

cd $USER_HOME/lambda_2
. ./set_up.sh

cd $USER_HOME/lambda_permission
. ./set_up.sh

cd $USER_HOME/test_lambda
. ./set_up.sh
