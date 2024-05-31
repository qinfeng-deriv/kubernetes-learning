# Kubernetes Lab 3

In this lab we are practising how to use helm to deploy `qinfengderiv/flask-app:2.0.0`.
This is a continuum from lab2.

## Overall flow of deploying to k8s using halem

Install helm first, if you haven't already.

## Specific steps
1) `helm create my-app-chart`
2) Change `my-app-chart/values.yaml` to
```
image:
  repository: qinfengderiv/flask-app
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: 2.0.0
```

3) Copy the existing deployment and service yaml files to `my-app-chart/templates`
4) Change `my-app-chart/templates/deployment.yaml` to 
```
    spec:
      containers:
        - name: flask-app
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```
This is to use the image name and tag dynamically from `values.yaml`

5) `helm install my-app-helm ./my-app-chart`
6) Your app should be deployed now! Notice how we don't have to `kubectl apply -f` anymore.

## Clean up
1) `helm uninstall my-app-helm`
