#!/bin/bash

if [ "$1" ==  "create" ];then

    clear
    echo "Creating Cluster"
    eksctl create cluster  --version=1.17 \
               --name=dev-eks \
               --region=us-east-1 \
               --zones=us-east-1a,us-east-1b \
	       --without-nodegroup

    eksctl utils associate-iam-oidc-provider \
        --region us-east-1 \
        --cluster dev-eks \
	--approve


    eksctl create nodegroup --cluster=dev-eks \
                        --region=us-east-1 \
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
			--alb-ingress-access

    echo "Cluster Created"
    eksctl get cluster

    kubectl get nodes

    echo "Bootstraping.."
    echo "Creating Autoscaler group"
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/autoscaler/master/cluster-autoscaler/cloudprovider/aws/examples/cluster-autoscaler-autodiscover.yaml
    eksctl utils install-vpc-controllers --cluster dev-eks --approve
    kubectl apply -f kube2iam.yaml
    

else 

    eksctl delete cluster dev-eks

fi
