#!/usr/bin/env python3
import sys
import os
ARGUMENT = sys.argv[1]
if ARGUMENT == "apply":
    CRDB = ("aws rds create-db-instance \
        --db-instance-identifier usermgmtdb \
        --db-instance-class db.t3.micro \
        --engine mysql \
        --master-username dbadmin \
        --master-user-password dbpassword11 \
	    --allocated-storage 20 \
	    --db-subnet-group-name eks-rds-db-subnetgroup
    os.system(CRDB)
elif ARGUMENT == "apply":
    CRDB = 
