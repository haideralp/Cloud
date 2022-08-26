# Uploading Content to S3

import boto3
s3_client = boto3.client('s3')
s3_client.upload_file('test.txt','eng122-haider-botobuck','test.txt')