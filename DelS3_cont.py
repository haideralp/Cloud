# Deleting Content In A S3 Bucket

import boto3

AWS_REGION = "eu-west-1"
S3_BUCKET_NAME = "eng122-haider-buck"

s3 = boto3.resource("s3", AWS_REGION)
obj = s3.Object("bucket_name", "filename.format")
obj.delete()

print('S3 object deleted')