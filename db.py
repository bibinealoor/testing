import requests
import json

instance_id = '1871036088967188.8.gcp.databricks.com'

api_version = '/api/2.0'
api_command = '/jobs/create'
url = f"https://{instance_id}{api_version}{api_command}"

response = requests.post(
  url = url,
  data = open('./create_job.json', 'rb')
)

print(json.dumps(json.loads(response.text), indent = 2))