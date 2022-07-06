# Orchestration with Kubernetes
This directory contains a deployment of the simple web application on Kubernetes using Minikube.

## Installation 
1. Clone this repository: ```git clone mralbertk/dsti-devops-final```
2. Install Virtualbox: [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
3. Install Docker: [Get Docker](https://docs.docker.com/get-docker/)
4. Install Minikube: [minikube start](https://minikube.sigs.k8s.io/docs/start/)

## Run
````shell
# Create a minikube cluster
minikube start 

# Deploy userapi to Kubernetes 
kubectl apply -f your/local/repository/k8s
````

### Note: For Windows Users
The deployment can be slightly more complicated when running on Windows:

1. Make sure VirtualBox and Docker are running on your system
2. Launch PowerShell **with Administrator privileges**
3. From the elevated shell, launch `minikube` with this extended command*:  

    `minikube start --driver=virtualbox --cpus=[int] --memory=[int] --no-vtx-check`  

3. Once minikube has started, create a new elevated PowerShell terminal and open a 
[minikube tunnel](https://minikube.sigs.k8s.io/docs/handbook/accessing/#using-minikube-service-with-tunnel): 

    `minikube tunnel`

4. Deploy userapi to Kubernetes as described above.
5. Get the external cluster IP and port as described above.

_*Note: Recommended specs for minikube are 1 CPUs and 2048 MB of memory but (much) more is better._

## Use 
- Get the external IP of the cluster: `kubectl get svc`
- Connect to FastAPI and Kubernetes using the external cluster IP and port (default 3000).
- For more information, refer to top-level [documentation](../README.md)

## Cleanup 
- Stop the minikube cluster: `minikube stop`
- Delete the minikube cluster: `minikube delete`

