#!/usr/bin/env bash

# Deploy example Nodeport
kubectl create deployment web --image=gcr.io/google-samples/hello-app:1.0
kubectl expose deployment web --type=NodePort --port=8080


# Deploy Loan Balancer
#kubectl create deployment helloworld --image=k8s.gcr.io/echoserver:1.4 --port=8080
#kubectl expose deployment helloworld --type=LoadBalancer