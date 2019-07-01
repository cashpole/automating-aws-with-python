# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='cashpolevideolyzervideos')
from pathlib import path
get_ipython().run_line_magic('ls', '~/downloads')
get_ipython().run_line_magic('ls', '~/downloads/*.mp4')
pathname = '~/Users/dawnashpole/downloads/Pexels Videos 2957.mp4'
path = Path(pathname).expanduser().resolve()
from pathlib import Path
path = Path(pathname).expanduser().resolve()
bucket.upload_file(str(path), str(path.name))
path
path.name
str(path)
pathname = '~/downloads/Pexels Videos 2957.mp4'
bucket.upload_file(str(path), str(path.name))
pathname = '~/Downloads/Pexels Videos 2957.mp4'
bucket.upload_file(str(path), str(path.name))
get_ipython().run_line_magic('ls', '~/Downloads/*.mp4')
pathname = '~/Downloads/Pexels Videos 2957.mp4'
path = Path(pathname).expanduser().resolve()
path
path.name
str(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={ 'S3Object': { 'Bucket': bucket.name, 'Name': path.name } } )
response
job_id = respone['JobId']
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['Lables']
result['Labels']
get_ipython().run_line_magic('pwd', '')
