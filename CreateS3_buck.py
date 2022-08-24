# Creating S3 in AWS - (Boto3)

import boto3
s3_client = boto3.client('s3')   #generating S3 client here to form connection
s3_client.create_bucket(Bucket='eng122-haider-botobuck',  # using create bucket bucket command to create bucket
CreateBucketConfiguration= {'LocationConstraint':'eu-west-1'}) # AWS requries us to be more specific so defining region