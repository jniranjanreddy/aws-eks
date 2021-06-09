# aws-eks
```
#How to install eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
mv eksctl /usr/local/bin/

#How to create EKS Cluster

#eksctl create cluster --name=niru-eks \
                      --region=us-east-1 \
					            --zones=us-east-1a,us-east-1b \
					            --without-nodegroup
            
2021-06-08 13:58:18 [ℹ]  eksctl version 0.52.0
2021-06-08 13:58:18 [ℹ]  using region us-east-1
2021-06-08 13:58:18 [ℹ]  subnets for us-east-1a - public:192.168.0.0/19 private:192.168.64.0/19
2021-06-08 13:58:18 [ℹ]  subnets for us-east-1b - public:192.168.32.0/19 private:192.168.96.0/19
2021-06-08 13:58:18 [ℹ]  using Kubernetes version 1.19
2021-06-08 13:58:18 [ℹ]  creating EKS cluster "niru-eks" in "us-east-1" region with
2021-06-08 13:58:18 [ℹ]  if you encounter any issues, check CloudFormation console or try 'eksctl utils describe-stacks --region=us-east-1 --cluster=niru-eks'
2021-06-08 13:58:18 [ℹ]  CloudWatch logging will not be enabled for cluster "niru-eks" in "us-east-1"
2021-06-08 13:58:18 [ℹ]  you can enable it with 'eksctl utils update-cluster-logging --enable-types={SPECIFY-YOUR-LOG-TYPES-HERE (e.g. all)} --region=us-east-1 --cluster=niru-eks'
2021-06-08 13:58:18 [ℹ]  Kubernetes API endpoint access will use default of {publicAccess=true, privateAccess=false} for cluster "niru-eks" in "us-east-1"
2021-06-08 13:58:18 [ℹ]  2 sequential tasks: { create cluster control plane "niru-eks", 2 sequential sub-tasks: { wait for control plane to become ready, 1 task: { create addons } } }
2021-06-08 13:58:18 [ℹ]  building cluster stack "eksctl-niru-eks-cluster"
2021-06-08 13:58:26 [ℹ]  deploying stack "eksctl-niru-eks-cluster"
2021-06-08 13:58:56 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 13:59:42 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:00:50 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:01:56 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:03:02 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:04:09 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:05:15 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:06:22 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:07:29 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:08:35 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:09:41 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:10:48 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:11:55 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:13:01 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-cluster"
2021-06-08 14:13:36 [ℹ]  waiting for the control plane availability...
2021-06-08 14:13:36 [✔]  saved kubeconfig as "/root/.kube/config"
2021-06-08 14:13:36 [ℹ]  no tasks
2021-06-08 14:13:36 [✔]  all EKS cluster resources for "niru-eks" have been created
2021-06-08 14:14:02 [ℹ]  kubectl command should work with "/root/.kube/config", try 'kubectl get nodes'
2021-06-08 14:14:02 [✔]  EKS cluster "niru-eks" in "us-east-1" region is ready
========================================================================================================
# eksctl utils associate-iam-oidc-provider \
        --region us-east-1 \
		    --cluster niru-eks \
		    --approve
2021-06-08 14:23:21 [ℹ]  eksctl version 0.52.0
2021-06-08 14:23:21 [ℹ]  using region us-east-1
2021-06-08 14:23:33 [ℹ]  will create IAM Open ID Connect provider for cluster "niru-eks" in "us-east-1"
2021-06-08 14:23:40 [✔]  created IAM Open ID Connect provider for cluster "niru-eks" in "us-east-1"
========================================================================================================
eksctl create nodegroup --cluster=niru-eks \
                        --region=us-east-1 \
						--name=niru-eks-ng-public1 \
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

2021-06-08 14:37:00 [ℹ]  eksctl version 0.52.0
2021-06-08 14:37:00 [ℹ]  using region us-east-1
2021-06-08 14:37:07 [ℹ]  will use version 1.19 for new nodegroup(s) based on control plane version
2021-06-08 14:37:29 [ℹ]  using EC2 key pair %!q(*string=<nil>)
2021-06-08 14:37:37 [ℹ]  1 nodegroup (niru-eks-ng-public1) was included (based on the include/exclude rules)
2021-06-08 14:37:37 [ℹ]  will create a CloudFormation stack for each of 1 managed nodegroups in cluster "niru-eks"
2021-06-08 14:37:37 [ℹ]  2 sequential tasks: { fix cluster compatibility, 1 task: { 1 task: { create managed nodegroup "niru-eks-ng-public1" } } }
2021-06-08 14:37:37 [ℹ]  checking cluster stack for missing resources
2021-06-08 14:37:38 [ℹ]  cluster stack has all required resources
2021-06-08 14:37:38 [ℹ]  building managed nodegroup stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:37:39 [ℹ]  deploying stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:37:39 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:37:55 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:38:19 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:38:45 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:39:07 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:39:33 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:39:59 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:40:24 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:40:48 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:41:12 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 14:41:19 [ℹ]  no tasks
2021-06-08 14:41:19 [✔]  created 0 nodegroup(s) in cluster "niru-eks"
2021-06-08 14:41:25 [ℹ]  nodegroup "niru-eks-ng-public1" has 2 node(s)
2021-06-08 14:41:25 [ℹ]  node "ip-192-168-30-234.ec2.internal" is ready
2021-06-08 14:41:25 [ℹ]  node "ip-192-168-61-255.ec2.internal" is ready
2021-06-08 14:41:25 [ℹ]  waiting for at least 2 node(s) to become ready in "niru-eks-ng-public1"
2021-06-08 14:41:25 [ℹ]  nodegroup "niru-eks-ng-public1" has 2 node(s)
2021-06-08 14:41:25 [ℹ]  node "ip-192-168-30-234.ec2.internal" is ready
2021-06-08 14:41:25 [ℹ]  node "ip-192-168-61-255.ec2.internal" is ready
2021-06-08 14:41:25 [✔]  created 1 managed nodegroup(s) in cluster "niru-eks"
2021-06-08 14:41:33 [ℹ]  checking security group configuration for all nodegroups
2021-06-08 14:41:33 [ℹ]  all nodegroups have up-to-date configuration
=============================================================================================================
Deleting EKS Cluster..
[root@minikube01 tmp]# eksctl delete cluster niru-eks
2021-06-08 15:37:47 [ℹ]  eksctl version 0.52.0
2021-06-08 15:37:47 [ℹ]  using region us-east-1
2021-06-08 15:37:47 [ℹ]  deleting EKS cluster "niru-eks"
2021-06-08 15:38:00 [ℹ]  deleted 0 Fargate profile(s)
2021-06-08 15:38:07 [✔]  kubeconfig has been updated
2021-06-08 15:38:07 [ℹ]  cleaning up AWS load balancers created by Kubernetes objects of Kind Service or Ingress
2021-06-08 15:38:36 [ℹ]  3 sequential tasks: { delete nodegroup "niru-eks-ng-public1", delete IAM OIDC provider, delete cluster control plane "niru-eks" [async] }
2021-06-08 15:38:36 [ℹ]  will delete stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:38:36 [ℹ]  waiting for stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1" to get deleted
2021-06-08 15:38:36 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:38:53 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:39:15 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:39:41 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:40:04 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:40:30 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:40:55 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:41:20 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:41:43 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:42:07 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:42:30 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:42:52 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:43:17 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:43:39 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-08 15:43:58 [ℹ]  will delete stack "eksctl-niru-eks-cluster"
2021-06-08 15:43:58 [✔]  all cluster resources were deleted
```
```
[root@minikube01 myworkspace]# eksctl get nodegroup --cluster niru-eks
2021-06-09 12:02:44 [ℹ]  eksctl version 0.52.0
2021-06-09 12:02:44 [ℹ]  using region us-east-1
CLUSTER         NODEGROUP               STATUS          CREATED                 MIN SIZE        MAX SIZE        DESIRED CAPACITY        INSTANCE TYPE   IMAGE ID   ASG NAME
niru-eks        niru-eks-ng-public1     ACTIVE          2021-06-09T06:18:31Z    2               3               2                       t3.medium       AL2_x86_64 eks-d4bcf7b6-0b46-44b0-0330-a64d4bb32e08
niru-eks        non-prod-1              CREATE_COMPLETE 2021-06-09T15:51:39Z    3               3               3                       t2.small        ami-0ef0c69399dbb5f3f      eksctl-niru-eks-nodegroup-non-prod-1-NodeGroup-1WLW8NIZLC2BP

```
