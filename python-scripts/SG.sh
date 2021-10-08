#!/bin/bash
EKSVPC=$(aws ec2 describe-vpcs | grep -i VpcId | head -1  | awk '{print $2}' | sed 's/"//g' | sed 's/,//g')
aws ec2 create-security-group \
--group-name eks_rds_db_sg \
--description "Allow access for RDS Database on Port 3306" \
--vpc-id "${EKSVPC}"

