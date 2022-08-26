# Amazon S3 Set Up - Client Method 

### Prerequistes Needed

- Pip3 must be installed --> sudo apt install python3-pip  (after checking for version with command **python --version**)
- Python Version 3.7 -> sudo apt-get install python -y  if version still showing set up alias python environment using **alias python=python3**
- AWS Command Line Interface - sudo pip3 install awscli
- AWS Access & Secret Key configurations --> **aws configure** * set region config: **eu-west-1** and output formant: **json**

For the steps below I have used the documentation from link to create python scripts for CRUD operations:

[Boto3 Official Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html?highlight=copy#S3.Client.copy)

### Creation of S3 Bucket

- Executing code below creates the S3. I have named my bucket: **eng122-haider-botobuck** 

'''   
import boto3
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket='eng122-haider-botobuck',
CreateBucketConfiguration= {'LocationConstraint':'eu-west-1'})
'''

![s3 create](https://user-images.githubusercontent.com/97620055/186361737-bcee11eb-c3d7-412f-9803-64408613447b.PNG)


### Uploading Content/File

- Executing code uploads the content to S3 bucket. 

'''
import boto3
s3_client = boto3.client('s3')
s3_client.upload_file('test.txt','eng122-haider-botobuck','test.txt')
'''
![upload](https://user-images.githubusercontent.com/97620055/186361790-314050f8-062b-47d7-a5be-1129515c038e.PNG)


### Retrieving Content/File

- Executing code below retrieves the content in the file and is renamed at destination. 

'''
import boto3
s3_client = boto3.client('s3')
s3_client.download_file('eng122-haider-botobuck', 'test.txt','retrieved_file.txt')
'''


![retrieved file](https://user-images.githubusercontent.com/97620055/186361849-7707fcb4-e5be-4a86-9af3-c60d7901ec5c.PNG)


###  Deleting Content/File

- Executing code below deletes the content in the file. 

'''
import boto3
s3_client = boto3.client('s3')
s3_client.delete_object(Bucket='eng122-haider-botobuck', Key='test.txt')
'''

![delete](https://user-images.githubusercontent.com/97620055/186361910-7459a72f-fee2-443b-8894-c747a9e96a16.PNG)


### Deleting S3 Bucket

- Executing code below deletes the S3 bucket. 

'''
import boto3
s3_client = boto3.client('s3')
s3_client.delete_bucket(Bucket='eng122-haider-botobuck')
'''

![image](https://user-images.githubusercontent.com/97620055/186370257-bb937d90-cb47-4a48-bcca-2abcc2da71e5.png)

#### Listing S3 Bucket - Extra Task