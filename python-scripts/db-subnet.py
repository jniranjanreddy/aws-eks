#!/usr/bin/env bash
aws rds create-db-subnet-group \
    --db-subnet-group-name eks-rds-db-subnetgroup \
    --db-subnet-group-description "EKS RDS DB Subnet Group" \
    --subnet-ids '["subnet-bd5c06f1","subnet-dec5a8a5","subnet-9bcd38f0"]'

#Delete
#aws rds delete-db-subnet-group --db-subnet-group-name eks-rds-db-subnetgroup