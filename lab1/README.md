# Kubernetes hands-on hello world project

This is just my study notes. Which the knowledge and steps may or may not be correct.

## Overall flow of deploying to k8s

Before this, you need to have your application containerize and by design, stateless.

1) Have a cluster running. In my case, it's Minikube.
2) Create deployment
3) Create service

## Specific steps
1) `kubectl apply -f app-deployment.yaml`
2) `kubectl apply -f service.yaml`
3) `minikube service my-app-service --url`
4) `curl` the URL from step 3


