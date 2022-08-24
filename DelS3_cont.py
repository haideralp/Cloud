# Deleting Content In A S3 Bucket

import boto3
s3_client = boto3.client('s3')
s3_client.delete_object(Bucket='eng122-haider-botobuck', Key='test.txt')