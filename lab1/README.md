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

## So, wtf did I just done
1) You can access your flask-app via Minikube url
```
(base) ➜  kubernetes-learning curl 127.0.0.1:59661
Hello, World!%
```
2) The cron job triggered at the specified interval
```
(base) ➜  kubernetes-learning git:(main) ✗ kubectl get pods
NAME                        READY   STATUS      RESTARTS   AGE
cron-job-1-28617630-pq9bg   0/1     Completed   0          26s
my-app-5f89b87f95-d2nqg     1/1     Running     0          5m39s

(base) ➜  kubernetes-learning git:(main) ✗ kubectl get cronjob
NAME         SCHEDULE      TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
cron-job-1   */5 * * * *   <none>     False     0        34s             5m1s
cron-job-2   0 0 * * *     <none>     False     0        <none>          5m1s
```

## Clean up
1) `kubectl delete service my-app-service`
2) `kubectl delete deployment my-app`
3) `kubectl delete cron-job-1`
4) `kubectl delete cron-job-2`
