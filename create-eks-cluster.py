#!/usr/bin/env python
import sys
import os
CLUSTER = "uat-eks"
# checking the argument 
ARGUMENT = sys.argv[1]
if ARGUMENT == "apply":
    print("apply")
    # Execute OS Commands
    command1 = ("eksctl create cluster  --version=1.17 \
               --name={} \
               --region=us-east-2 \
               --zones=us-east-2a,us-east-2b \
               --without-nodegroup".format(CLUSTER))
    os.system(command1)
    command2 = ("eksctl utils associate-iam-oidc-provider \
               --region us-east-2 \
               --cluster {} \
               --approve".format(CLUSTER))
    os.system(command2)
    command3 = ("eksctl create nodegroup --cluster={} \
               --region=us-east-2 \
               --name=dev-eks-ng-public1 \
               --node-type=t3.medium \
               --nodes=2 \
               --nodes-min=2 \
               --nodes-max=4 \
               --node-volume-size=20 \
               --ssh-access \
               --ssh-public-key=kube-demo \
               --managed \
               --asg-access \
               --external-dns-access \
               --full-ecr-access \
               --appmesh-access \
               --alb-ingress-access".format(CLUSTER))
    os.system(command3)
    command4 = ("eksctl get cluster ; kubectl get nodes")
    os.system(command4)

elif ARGUMENT  == "destroy":
    print("destroy")
    command5 = ("eksctl delete cluster {}".format(CLUSTER))
    os.system(command5)
else:
    print("execute: " + sys.argv[0] + " apply/destroy")
