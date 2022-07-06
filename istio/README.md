# Service Mesh with Istio

## Installation 
1. Clone this repository: ```git clone mralbertk/dsti-devops-final```
2. Install Virtualbox: [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
3. Install Docker: [Get Docker](https://docs.docker.com/get-docker/)
4. Install Minikube: [minikube start](https://minikube.sigs.k8s.io/docs/start/)
5. Download Istio: [Istio: Getting Started](https://istio.io/latest/docs/setup/getting-started/)

## Run
````shell
# Create a minikube cluster with sufficient resources
minikube start --cpus=4 --memory=16384

# Install Istio to your minikube cluster
istioctl install --set profile=default -y

# Enable Istio envoy injection on the desired namespace
kubectl label namespace my-namespace istio-injection=enabled

# Deploy userapi to cluster 
kubectl apply -f your/local/repository/istio/userapi-python.yml -n my-namespace

# DeployIistio service mesh to cluster
kubectl apply -f your/local/repository/istio/userapi-gateway.yml -n my-namespace
````

### Note: For Windows Users
- Refer to the [Kubernetes deployment instructions](../k8s/README.md) for details


## Use
- Get the ingress-IP of the cluster: `kubectl get svc -n istio-system`
- Access the IP via a browser to interact with the API 
- For more information, refer to top-level [documentation](../README.md)

## Cleanup 
- Stop the minikube cluster: `minikube stop`
- Delete the minikube cluster: `minikube delete`