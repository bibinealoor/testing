A **main.py** file contains the python code to be run and is supported by config file **app_config.json** that supplies variables into *main.py* 

main.py takes two arguments 1.App Name 2.dbfs path to app_config.json 

The arguments are passed through Databricks job. If main.py is run through an IDE for testing, follow the option available to the respective IDE to pass in the arguments. 
Command line example is shown below

`python main.py <arg1> <arg2>`

**create_job.json** file will be used to create a Databricks job that can execute the app i.e., main.py. A schedule can be included for Databricks to run the job on schedule. Alternately the job can be triggered manually through Databricks console or through another orchestration tool e.g., Airflow by using the Databricks API / CLI
*main.py* should be uploaded to a dbfs file path and included in the *create_job.json*

The deployment steps are - 

* Copy main.py to target dbfs path `e.g., dbfs:/mnt/code/<app short name>/main.py`
* Copy app_config.json to the target dbfs path `e.g., dbfs:/mnt/code/<app short name>/app_config.json`
* Execute Databricks Create/update job command / API by supplying the *create_job.json* settings file
* If the job is created for the first time then update *create_job.json* to include the **Job Id** as Job Id is required for further interaction with the job
