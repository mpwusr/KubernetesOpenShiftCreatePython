import requests
import json
import os
import yaml

# Load resource definition from file
with open("deployment.yaml", "r") as f:
    resource = yaml.safe_load(f)

# OpenShift API
API_SERVER = "https://api.openshift.example.com:6443"
NAMESPACE = "default"
TOKEN = os.environ["BEARER_TOKEN"]
CA_CERT = "/path/to/ca.crt"

# Determine the API endpoint (based on kind)
kind = resource["kind"].lower()
api_path = "apis/apps/v1" if kind == "deployment" else "api/v1"
url = f"{API_SERVER}/{api_path}/namespaces/{NAMESPACE}/{kind}s"

# Send POST request
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
response = requests.post(url, headers=headers, json=resource, verify=CA_CERT)

print("Status:", response.status_code)
print(response.json())
