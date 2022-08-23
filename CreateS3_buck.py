# Creating S3 in AWS - (Boto3)

import boto3

client = boto3.client('s3')

bucket_name=str(input('Please input bucket name to be created: '))

#Bucket Name argument is mandatory and bucket name should be unique
response1 = client.create_bucket(
    ACL='public',                    # amazon access control lists - allows you manage permissions of your bucket and who has access.
    Bucket=bucket_name
    )

print(response1['Location'])