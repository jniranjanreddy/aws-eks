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
#How to create a new NodeGroup
[root@minikube01 myworkspace]# cat node-group.yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: niru-eks
  region: us-east-1

nodeGroups:
  - name: non-prod-1
    instanceType: t2.small
    desiredCapacity: 3
    ssh: # use existing EC2 key
      publicKeyName: kube-demo

###Before adding NodeGroup
[root@minikube01 ~]# kubectl get nodes
NAME                            STATUS   ROLES    AGE   VERSION
ip-192-168-17-63.ec2.internal   Ready    <none>   9h    v1.19.6-eks-49a6c0
ip-192-168-50-92.ec2.internal   Ready    <none>   8h    v1.19.6-eks-49a6c0

[root@minikube01 myworkspace]# eksctl create nodegroup --config-file=node-group.yaml --include='non-prod-1'
2021-06-09 11:50:54 [ℹ]  eksctl version 0.52.0
2021-06-09 11:50:54 [ℹ]  using region us-east-1
2021-06-09 11:51:00 [ℹ]  will use version 1.19 for new nodegroup(s) based on control plane version
2021-06-09 11:51:29 [ℹ]  nodegroup "non-prod-1" will use "ami-0ef0c69399dbb5f3f" [AmazonLinux2/1.19]
2021-06-09 11:51:29 [ℹ]  using EC2 key pair "kube-demo"
2021-06-09 11:51:37 [ℹ]  1 existing nodegroup(s) (niru-eks-ng-public1) will be excluded
2021-06-09 11:51:37 [ℹ]  combined include rules: non-prod-1
2021-06-09 11:51:37 [ℹ]  1 nodegroup (non-prod-1) was included (based on the include/exclude rules)
2021-06-09 11:51:37 [ℹ]  will create a CloudFormation stack for each of 1 nodegroups in cluster "niru-eks"
2021-06-09 11:51:38 [ℹ]  2 sequential tasks: { fix cluster compatibility, 1 task: { 1 task: { create nodegroup "non-prod-1" } } }
2021-06-09 11:51:38 [ℹ]  checking cluster stack for missing resources
2021-06-09 11:51:39 [ℹ]  cluster stack has all required resources
2021-06-09 11:51:39 [ℹ]  building nodegroup stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:51:39 [ℹ]  --nodes-min=3 was set automatically for nodegroup non-prod-1
2021-06-09 11:51:39 [ℹ]  --nodes-max=3 was set automatically for nodegroup non-prod-1
2021-06-09 11:51:40 [ℹ]  deploying stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:51:40 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:51:56 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:52:19 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:52:45 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:53:08 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:53:34 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:53:59 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:54:24 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:54:47 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:55:11 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:55:43 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:56:06 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:56:31 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-non-prod-1"
2021-06-09 11:56:38 [ℹ]  no tasks
2021-06-09 11:56:43 [ℹ]  adding identity "arn:aws:iam::936766936551:role/eksctl-niru-eks-nodegroup-non-pro-NodeInstanceRole-148JVGRGN0LHO                           " to auth ConfigMap
2021-06-09 11:56:44 [ℹ]  nodegroup "non-prod-1" has 0 node(s)
2021-06-09 11:56:44 [ℹ]  waiting for at least 3 node(s) to become ready in "non-prod-1"
2021-06-09 11:57:30 [ℹ]  nodegroup "non-prod-1" has 3 node(s)
2021-06-09 11:57:30 [ℹ]  node "ip-192-168-15-198.ec2.internal" is ready
2021-06-09 11:57:30 [ℹ]  node "ip-192-168-22-1.ec2.internal" is ready
2021-06-09 11:57:30 [ℹ]  node "ip-192-168-40-22.ec2.internal" is ready
2021-06-09 11:57:30 [✔]  created 1 nodegroup(s) in cluster "niru-eks"
2021-06-09 11:57:30 [✔]  created 0 managed nodegroup(s) in cluster "niru-eks"
2021-06-09 11:57:39 [ℹ]  checking security group configuration for all nodegroups
2021-06-09 11:57:39 [ℹ]  all nodegroups have up-to-date configuration

### After adding New NodeGroup
[root@minikube01 myworkspace]# k get nodes
NAME                             STATUS   ROLES    AGE    VERSION
ip-192-168-15-198.ec2.internal   Ready    <none>   103s   v1.19.6-eks-49a6c0
ip-192-168-17-63.ec2.internal    Ready    <none>   9h     v1.19.6-eks-49a6c0
ip-192-168-22-1.ec2.internal     Ready    <none>   103s   v1.19.6-eks-49a6c0
ip-192-168-40-22.ec2.internal    Ready    <none>   107s   v1.19.6-eks-49a6c0
ip-192-168-50-92.ec2.internal    Ready    <none>   9h     v1.19.6-eks-49a6c0



[root@minikube01 myworkspace]# eksctl get nodegroup --cluster niru-eks
2021-06-09 12:02:44 [ℹ]  eksctl version 0.52.0
2021-06-09 12:02:44 [ℹ]  using region us-east-1
CLUSTER    NODEGROUP               STATUS   CREATED                 MIN SIZE  MAX SIZE   DESIRED CAPACITY    INSTANCE TYPE   IMAGE ID   ASG NAME
niru-eks   niru-eks-ng-public1     ACTIVE   2021-06-09T06:18:31Z    2         3          2                   t3.medium       AL2_x86_64 eks-d4bcf7b6-0b46-44b0-0330-a64d4bb32e08
niru-eks   non-prod-1       CREATE_COMPLETE 2021-06-09T15:51:39Z    3         3          3                   t2.small        ami-0ef0c69399dbb5f3f      eksctl-niru-eks-nodegroup-non-prod-1-NodeGroup-1WLW8NIZLC2BP

```
```
[root@minikube01 myworkspace]# eksctl get nodegroup --cluster niru-eks
2021-06-09 16:30:56 [ℹ]  eksctl version 0.52.0
2021-06-09 16:30:56 [ℹ]  using region us-east-1
CLUSTER         NODEGROUP               STATUS          CREATED                 MIN SIZE        MAX SIZE        DESIRED CAPACITY        INSTANCE TYPE   IMAGE ID   ASG NAME
niru-eks        niru-eks-ng-public1     ACTIVE          2021-06-09T06:18:31Z    2               3               2                       t3.medium       AL2_x86_64 eks-d4bcf7b6-0b46-44b0-0330-a64d4bb32e08
niru-eks        non-prod-1              CREATE_COMPLETE 2021-06-09T15:51:39Z    3               3               3                       t2.small        ami-0ef0c69399dbb5f3f       eksctl-niru-eks-nodegroup-non-prod-1-NodeGroup-1WLW8NIZLC2BP
niru-eks        non-prod-2              CREATE_COMPLETE 2021-06-09T19:45:16Z    1               1               1                       t2.small        ami-0ef0c69399dbb5f3f       eksctl-niru-eks-nodegroup-non-prod-2-NodeGroup-5BDCRYDII9JC
niru-eks        non-prod-managed        `ACTIVE`          2021-06-09T20:25:36Z    1               4               1                       t3.medium       AL2_x86_64 eks-aabcf939-d0a4-ed4c-7420-f6460828ab84
[root@minikube01 myworkspace]#
```

```
#Update Nodegroup...

[root@minikube01 ~]# eksctl upgrade nodegroup --name=niru-eks-ng-public1 --cluster=niru-eks --kubernetes-version=1.18
2021-06-10 07:44:29 [ℹ]  upgrading nodegroup version
2021-06-10 07:44:29 [ℹ]  updating nodegroup stack
2021-06-10 07:44:36 [ℹ]  waiting for CloudFormation changeset "eksctl-update-nodegroup-1623325469" for stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:44:53 [ℹ]  waiting for CloudFormation changeset "eksctl-update-nodegroup-1623325469" for stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:45:00 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:45:18 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:45:44 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:46:10 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:46:32 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:46:56 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:47:20 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:47:43 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:48:06 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:48:28 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:48:50 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:49:12 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:49:37 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:50:03 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:50:28 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:50:54 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:51:16 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:51:38 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:52:02 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:52:24 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:52:47 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:53:13 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:53:40 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:54:06 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:54:31 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:54:57 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:55:20 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:55:46 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:56:09 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:56:35 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:56:56 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:57:18 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:57:43 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:58:06 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:58:29 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:58:51 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:59:14 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 07:59:38 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 08:00:03 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 08:00:25 [ℹ]  waiting for CloudFormation stack "eksctl-niru-eks-nodegroup-niru-eks-ng-public1"
2021-06-10 08:00:31 [ℹ]  nodegroup successfully upgraded
[root@minikube01 ~]#

##While updating Cluster, we can observe the status chage..
[root@minikube01 ~]# k get nodes
NAME                             STATUS   ROLES    AGE     VERSION
ip-192-168-13-161.ec2.internal   Ready    <none>   3h5m    v1.17.12-eks-7684af
ip-192-168-28-190.ec2.internal   Ready    <none>   3h17m   v1.17.12-eks-7684af
ip-192-168-45-211.ec2.internal   Ready    <none>   3h17m   v1.17.12-eks-7684af
ip-192-168-53-133.ec2.internal   Ready    <none>   3h5m    v1.17.12-eks-7684af


[root@minikube01 ~]# k get nodes
NAME                             STATUS     ROLES    AGE     VERSION
ip-192-168-13-161.ec2.internal   Ready      <none>   3h9m    v1.17.12-eks-7684af
ip-192-168-15-170.ec2.internal   NotReady   <none>   12s     v1.18.9-eks-d1db3c
ip-192-168-28-190.ec2.internal   Ready      <none>   3h21m   v1.17.12-eks-7684af
ip-192-168-44-83.ec2.internal    NotReady   <none>   12s     v1.18.9-eks-d1db3c
ip-192-168-45-211.ec2.internal   Ready      <none>   3h21m   v1.17.12-eks-7684af
ip-192-168-53-133.ec2.internal   Ready      <none>   3h9m    v1.17.12-eks-7684af


[root@minikube01 ~]# k get nodes
NAME                             STATUS                     ROLES    AGE     VERSION
ip-192-168-13-161.ec2.internal   Ready                      <none>   3h12m   v1.17.12-eks-7684af
ip-192-168-15-170.ec2.internal   Ready                      <none>   2m58s   v1.18.9-eks-d1db3c
ip-192-168-28-190.ec2.internal   Ready,SchedulingDisabled   <none>   3h24m   v1.17.12-eks-7684af
ip-192-168-44-83.ec2.internal    Ready                      <none>   2m58s   v1.18.9-eks-d1db3c
ip-192-168-45-211.ec2.internal   Ready                      <none>   3h24m   v1.17.12-eks-7684af
ip-192-168-53-133.ec2.internal   Ready                      <none>   3h12m   v1.17.12-eks-7684af


[root@minikube01 ~]# k get nodes
NAME                             STATUS                     ROLES    AGE     VERSION
ip-192-168-0-46.ec2.internal     NotReady                   <none>   26s     v1.18.9-eks-d1db3c
ip-192-168-13-161.ec2.internal   Ready                      <none>   3h14m   v1.17.12-eks-7684af
ip-192-168-15-170.ec2.internal   Ready                      <none>   5m5s    v1.18.9-eks-d1db3c
ip-192-168-44-83.ec2.internal    Ready                      <none>   5m5s    v1.18.9-eks-d1db3c
ip-192-168-45-211.ec2.internal   Ready,SchedulingDisabled   <none>   3h26m   v1.17.12-eks-7684af
ip-192-168-53-133.ec2.internal   Ready                      <none>   3h14m   v1.17.12-eks-7684af


[root@minikube01 ~]# k get nodes
NAME                             STATUS     ROLES    AGE     VERSION
ip-192-168-0-46.ec2.internal     Ready      <none>   2m32s   v1.18.9-eks-d1db3c
ip-192-168-13-161.ec2.internal   Ready      <none>   3h16m   v1.17.12-eks-7684af
ip-192-168-15-170.ec2.internal   Ready      <none>   7m11s   v1.18.9-eks-d1db3c
ip-192-168-44-83.ec2.internal    Ready      <none>   7m11s   v1.18.9-eks-d1db3c
ip-192-168-51-65.ec2.internal    NotReady   <none>   29s     v1.18.9-eks-d1db3c
ip-192-168-53-133.ec2.internal   Ready      <none>   3h16m   v1.17.12-eks-7684af

[root@minikube01 ~]# k get nodes
NAME                             STATUS                     ROLES    AGE     VERSION
ip-192-168-0-46.ec2.internal     Ready,SchedulingDisabled   <none>   5m25s   v1.18.9-eks-d1db3c
ip-192-168-13-161.ec2.internal   Ready                      <none>   3h19m   v1.17.12-eks-7684af
ip-192-168-15-170.ec2.internal   Ready                      <none>   10m     v1.18.9-eks-d1db3c
ip-192-168-44-83.ec2.internal    Ready                      <none>   10m     v1.18.9-eks-d1db3c
ip-192-168-53-133.ec2.internal   Ready                      <none>   3h19m   v1.17.12-eks-7684af


#Final status, after updating..
[root@minikube01 ~]# k get nodes
NAME                             STATUS   ROLES    AGE     VERSION
ip-192-168-13-161.ec2.internal   Ready    <none>   3h22m   v1.17.12-eks-7684af
ip-192-168-15-170.ec2.internal   Ready    <none>   13m     v1.18.9-eks-d1db3c
ip-192-168-44-83.ec2.internal    Ready    <none>   13m     v1.18.9-eks-d1db3c
ip-192-168-53-133.ec2.internal   Ready    <none>   3h22m   v1.17.12-eks-7684af
```
