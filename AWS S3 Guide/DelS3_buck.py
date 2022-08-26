# Deleting S3 Bucket With 0 files - AWS

import boto3
s3_client = boto3.client('s3')
s3_client.delete_bucket(Bucket='eng122-haider-botobuck')