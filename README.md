# Repositório do projeto de microserviços da fiap

## Docker compose

### Como subir os sistemas

```bash
docker-compose up
```

### Como parar os sistemas

```bash
docker-compose down
```  

#### Como saber se as apis subiram?

Cada api tem um endpoint de healthcheck:

Api1:
```
curl http://localhost:8080/health
```

Api2:
```
curl http://localhost:8081/health
```

#### Como testar a comunicação entre as apis?

curl http://localhost:8080/outra-api

## Kubernetes

### Como subir os sistemas

```bash
kubectl apply -f k8s/api1-service.yaml
kubectl apply -f k8s/api2-service.yaml
kubectl apply -f k8s/api1-deployment.yaml
kubectl apply -f k8s/api2-deployment.yaml
```

### Como parar os sistemas

```bash
kubectl delete -f k8s/api1-service.yaml
kubectl delete -f k8s/api2-service.yaml
kubectl delete -f k8s/api1-deployment.yaml
kubectl delete -f k8s/api2-deployment.yaml
```

#### Como saber se as apis subiram?


```bash
kubectl get all
```

Para bater na api pegue o ip do service da api1 por exemplo: "10.101.82.3"
E bata no health check:

```bash
curl http://10.101.82.3:8080/health
``` 

Caso esteja usando o minikube, você pode precisar expor a url com o comando

```bash
minikube service --url api1
``` 

E utilizá-la no lugar de "http://10.101.82.3:8080"

#### Como testar a comunicação entre as apis?


Com o ip do service da api1:

```bash
curl http://10.101.82.3:8080/outra-api
```