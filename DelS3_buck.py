# Deleting S3 Bucket With 0 files - AWS

import boto3

client = boto3.client('s3')

bucket_name=str(input('Please input bucket name to be deleted: '))

print("Before deleting the bucket we need to check if its empty. Checking ...")

objs = client.list_objects_v2(Bucket=bucket_name)
fileCount = objs['KeyCount']

if fileCount == 0:  # using if look here to determine whether number of files = 0
    response = client.delete_bucket(Bucket=bucket_name) # response is produced to delete specified bucket
    print("{} has been deleted successfully !!!".format(bucket_name)) # message is then printed to say bucket has been deleted. 
else:
    print("{} is not empty {} objects present".format(bucket_name,fileCount)) # if filecount condition of 0 is not met. Print bucket name with number of files.
    print("Please make sure S3 bucket is empty before deleting it !!!") # print message for user telling them to empty bucket. 