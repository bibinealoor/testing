#!/bin/bash

gsutil cp app_config.json gs://db-testing-bucket/config
gsutil cp main.py gs://db-testing-bucket/python
pip3 install virtualenv
virtualenv env 
source env/bin/activate
pip3 install requests google-cloud-secret-manager
python3 db.py
