Setup commands (when using minikube):

Use local docker images in the minikube cluster
```bash
eval $(minikube docker-env) 
```

Build docker images
```bash
docker build -t devops-sig-app .
docker build -t config-renderer ./env-rendering/ 
```

Apply configmap and app pod:
```bash
kubectl apply -f env-rendering/configmap-myapp.yml  
kubectl apply -f env-rendering/myapp.yml
```

To observe results, forward minikube ports in one shell:
```bash
kubectl port-forward myapp-pod 8083:8000 
```

In another shell:
```
curl localhost:8083/var
```

And see value from the configmap

No dynamic updates yet, work in progress


