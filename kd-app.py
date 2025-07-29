from flask import Flask, request, jsonify
from kubernetes import client, config
import uuid

app = Flask(__name__)

# Load Kubernetes configuration
config.load_kube_config()

# Kubernetes API client
v1 = client.CoreV1Api()

@app.route('/deploy', methods=['POST'])
def deploy():
    data = request.json
    image = data.get('image')
    if not image:
        return jsonify({'error': 'Image reference is required'}), 400

    # Generate a unique name for the pod
    pod_name = f"pod-{uuid.uuid4()}"

    # Define the pod specification
    pod_spec = client.V1Pod(
        metadata=client.V1ObjectMeta(name=pod_name),
        spec=client.V1PodSpec(
            containers=[client.V1Container(name="container", image=image)],
            restart_policy="Never"
        )
    )

    # Create the pod in the default namespace
    try:
        v1.create_namespaced_pod(namespace="default", body=pod_spec)
        return jsonify({'message': 'Pod created', 'pod_name': pod_name}), 201
    except client.exceptions.ApiException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/status/<pod_name>', methods=['GET'])
def status(pod_name):
    try:
        pod = v1.read_namespaced_pod(name=pod_name, namespace="default")
        status = pod.status.phase
        return jsonify({'pod_name': pod_name, 'status': status}), 200
    except client.exceptions.ApiException as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

