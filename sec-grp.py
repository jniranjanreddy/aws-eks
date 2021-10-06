#!/usr/bin/env python3
import sys
import os
import subprocess
CLUS_NAME = sys.argv[1]
createSG = ("aws ec2 create-security-group \
           --group-name eks_rds_db_sg \
           --description 'Allow access for RDS Database on Port 3306' \
           --vpc-id eksctl-{}-cluster/VPC".format(CLUS_NAME))
os.system(createSG)


#eksctl-rama-prod-cluster/VPC
#eksctl-rama-prod-cluster/VPC
