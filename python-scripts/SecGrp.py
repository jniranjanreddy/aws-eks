#!/usr/bin/env python3
import sys
import os
firstARG = sys.argv[1]
vpcID = sys.argv[2]
if firstARG == "apply":
    CMD1 = ("aws ec2 create-security-group \
        --group-name eks_rds_db_sg \
        --description 'Allow access for RDS Database on Port 3306' \
        --vpc-id {}".format(vpcID))
    os.system(CMD1)
elif firstARG  == "destroy":
    CMD2 = ("aws ec2 delete-security-group --group-id {}".format(vpcID))
    os.system(CMD2)
else:
    print("execute: " + sys.argv[0] + " apply/destroy VPC-ID/Security Group")