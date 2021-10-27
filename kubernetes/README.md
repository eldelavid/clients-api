# Kubernetes
Kubernetes manifiests files to deploy client-api as well as elasticsearch+kibana stack.

## Prerequisities

## Download kubectl
```
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin
```

## Download the aws-iam-authenticator

See https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html


## Configure kubectl
```
terraform output kubeconfig # save output in ~/.kube/config
aws eks --region <region> update-kubeconfig --name terraform-eks-demo
```

## Configure config-map-auth-aws
```
terraform output config-map-aws-auth # save output in config-map-aws-auth.yaml
kubectl apply -f config-map-aws-auth.yaml
```

## See nodes coming up
```
kubectl get nodes
```
