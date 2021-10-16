#! /bin/sh

# **Do not** do this.
#curl -u <your-username>:<your-password> -X GET https://<databricks-instance>/api/2.0/clusters/list

curl -u $host_id:$token_id -X GET https://1871036088967188.8.gcp.databricks.com/api/2.0/jobs/create