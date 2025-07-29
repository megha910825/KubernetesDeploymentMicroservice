# Kubernetes Deployment Microservice

## Overview

This project is a minimal Python-based microservice that automates the deployment of public Docker images to a Kubernetes cluster and provides real-time status updates of the deployed pods. It is built using Flask for the API endpoints and the Kubernetes Python client for interacting with the Kubernetes API.

## Features

- **Deployment Endpoint**: Receives a Docker image reference and deploys it as a pod in the Kubernetes cluster.
- **Status Endpoint**: Provides the current status of the deployed pod, including its lifecycle state (e.g., Running, Pending, Failed).

## Technology Stack

- Python
- Flask
- Kubernetes Python client

## Setup Instructions

### Prerequisites

- Python 3.x
- Access to a Kubernetes cluster
- `kubectl` configured to interact with your cluster

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/megha910825/KubernetesDeploymentMicroservice.git
   cd KubernetesDeploymentMicroservice
    ```
2. Create a virtual environment and activate it:
3. 
   ```bash
     python3 -m venv k8s-microservice-env
     source k8s-microservice-env/bin/activate
   ```
4. Install the required packages:
   
   ```bash
     pip install flask kubernetes
   ```
### Running the Microservice
1. Start the Flask application
   ```bash
      python microservice.py
   ```
### Usage
1. Deploy the Pod
   To deploy a pod using a Docker image, send a POST request to the /deploy endpoint:
     ```bash
        curl -X POST http://localhost:5000/deploy -H "Content-Type: application/json" -d '{"image": "nginx"}'
      ```
2. Check Pod Status
   To check the status of a deployed pod, send a GET request to the /status/<pod_name> endpoint:
   ```bash
      curl http://localhost:5000/status/<pod_name>
   ```
### Testing
To run the tests, execute the following command:
```bash
   python -m unittest test_microservice.py
```
### Notes
- Ensure your Kubernetes cluster is accessible and configured correctly.
- The microservice assumes the default namespace for simplicity. You can extend it to support other namespaces.
- Error handling and logging can be improved for production use.

    
