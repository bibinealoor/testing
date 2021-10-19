import requests
import json
#git b3
instance_id = '1871036088967188.8.gcp.databricks.com'
api_version = '/api/2.0'
job_name = 'Sample1_schedule'
project_id = "zebra-cicd-327507"
secret_id = "brick-sec-1"
version_id = 1
def access_secret_version(project_id, secret_id, version_id):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager
    import json
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})

    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    pd = response.payload.data.decode("UTF-8")
    return json.loads(pd)

def create_job():
   api_command = '/jobs/create'
   url = f"https://{instance_id}{api_version}{api_command}"
   acc_token=access_secret_version(project_id, secret_id, version_id)
   response = requests.post(url, auth=(acc_token["login"], acc_token['password']), data = open('./create_job.json', 'rb'))
   print(json.dumps(json.loads(response.text), indent = 2))

def reset_job():
   api_command = '/jobs/reset'
   url = f"https://{instance_id}{api_version}{api_command}"
   acc_token=access_secret_version(project_id, secret_id, version_id)
   response = requests.post(url, auth=(acc_token["login"], acc_token['password']), data = open('./create_job.json', 'rb'))
   print(json.dumps(json.loads(response.text), indent = 2))


def list_job():
   api_command = '/jobs/list'
   url = f"https://{instance_id}{api_version}{api_command}"  
   acc_token=access_secret_version(project_id, secret_id, version_id)
   response = requests.get(url, auth=(acc_token["login"], acc_token['password']))
   a=json.dumps(json.loads(response.text), indent = 2)
#   print(a)
   if a == '{}':
      return False
   elif a != "{}":
      b=json.loads(a)
      f=[]
      for i in b['jobs']:
         f.append(i['settings']['name'])
      print("these jobs are exist", f)
      if job_name in f:
          job=True
          
      else:
          job=False
      return job
   else:
      return False

def main():
   status=list_job()
   if status == True:
#      reset_job()
      pass
   else:
      create_job() 

def get_job():
   api_command = '/jobs/get'
   url = f"https://{instance_id}{api_version}{api_command}"  
   acc_token=access_secret_version(project_id, secret_id, version_id)   
   params = {"job_id":'Sample3_schedule'}
   response = requests.get(url, auth=(acc_token["login"], acc_token['password']), params = params)
   a=json.dumps(json.loads(response.text), indent = 2)
   print(a)

#create_job()
#list_job()
main()
#reset_job()
#get_job()
