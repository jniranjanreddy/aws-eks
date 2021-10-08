#!/usr/bin/env python3
import sys
import os
#First Argument should be Security Group.
ingSGroup = sys.argv[1]
CMD1 = ("aws ec2 authorize-security-group-ingress \
        --group-id {} \
        --protocol tcp \
        --port 3306 \
        --cidr '0.0.0.0/0'".format(ingSGroup))
os.system(CMD1)