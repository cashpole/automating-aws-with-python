# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2019-07-01T16:27:33.149Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDA4RZDUYQMU4FIJNPFB'}, 'requestParameters': {'sourceIPAddress': '24.7.223.218'}, 'responseElements': {'x-amz-request-id': '389E6D967E505520', 'x-amz-id-2': 'VsVB4gXVOVE1qfzAar7NPFLLK3nOzCiAM7EtO9lr6d0Jbd0uqam32wEhes2rTvqrpOyczV+2Sps='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'dbf780f5-ee02-49c7-8dc1-6747d4457416', 'bucket': {'name': 'cashpolevideolyzer12345', 'ownerIdentity': {'principalId': 'A1LNENSZXJCKZ5'}, 'arn': 'arn:aws:s3:::cashpolevideolyzer12345'}, 'object': {'key': 'Pexels+Videos+1466210.mp4', 'size': 10687399, 'eTag': '5c4faa5961cc2989095699f89d501c66-2', 'sequencer': '005D1A34645A1F7114'}}}]}
event
event['Records'][0]
event['Records'][0]['bucket']['name']
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
