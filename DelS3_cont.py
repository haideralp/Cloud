# Deleting Content In A S3 Bucket

import boto3
s3 = boto3.resource("s3")
obj = s3.Object("bucket_name", "filename.format")
obj.delete()