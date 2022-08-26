# Retrieving Content from S3

import boto3
s3_client = boto3.client('s3')
s3_client.download_file('eng122-haider-botobuck', 'test.txt','retrieved_file.txt') #destination specified new filename