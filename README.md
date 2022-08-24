# Cloud Computing

## AWS - Best Practices To Implement: 
 - Naming convention eng_122_haider_ec2
 - AWS services to be used between 09:00 - 18:00 stop or terminate
 - If your need to use it out of hours please ask
 - WE MUST ONLY USE IRELAND.
 - terminate services once you finished working. 
 - Do not delete anyone else's services
 - MUST NOT SHARE AWS ACCOUNT DETAILS WITH ANYONE - SO NO GITHUB REPO 
 
 ## Powerpoint Explaining Cloud Computing & Models :
 
 https://github.com/haideralp/Cloud/blob/main/AWs%20PPT.pptx
 
# Overview Diagram Showcasing EC2 Creation on AWS  

![image](https://user-images.githubusercontent.com/97620055/185412695-2eca3fc1-e03a-4b1f-a37c-1148d8b6b7a2.png)

 
 * We would like to take monolithic artichiture and migrate to cloud. Prevent slower load ups / reduce error. 
 * Have data available outside cloud so you can initialise to Vms despite destroying it. As monolithic if you destroy all is gone. 
  
## Creating EC2 Instance On AWS
1. Once logged in check location is always set to **IRELAND**.
2. Select EC2 (if you cannot find it use search bar). Stick to opting into viewing with older experience (top right of browser). 
3. Select version of OS to generate the Vm (instance) {AMI Image Selection}. -->  **Ubuntu Server 18.04 LTS (HVM), SSD Volume Type - 64 bit (x86)**
4. Select the CPU configs or type of instance you desire.{Instance Type} --> **t2.micro (- ECUs, 1 vCPUs, 2.5 GHz, -, 1 GiB memory, EBS only)**
5. Configure the instance details as per requirments specified. For interest in my case study just modified the **subnet** and **assigned public ip** - see below.

![image](https://user-images.githubusercontent.com/97620055/185416950-eef4ae46-6f70-45a7-8eb0-b14a6844807c.png)

6.Add storage configs as per requirements. I kept this simple for this case. 

![image](https://user-images.githubusercontent.com/97620055/185417270-29d96907-c351-494f-9df9-2031a5bb126c.png)

7.Assing tags (key-value pairs) so it is identifiable on AWS. This can be extended to instances, volumes, network interfaces.

![image](https://user-images.githubusercontent.com/97620055/185417759-2a8718b3-64f2-4b59-831e-68ae0485918e.png)

8.Now the system requires me to configure the firewall settings with relevant ports and rules. For simplicity I have done the below:

![image](https://user-images.githubusercontent.com/97620055/185419529-ecbc1df6-78c6-40f1-958b-72f028eab5a0.png)

9. You do final review of the settings you have configured. In this case it was simple set-up. You then launch the instance by accepting that you have the private key in your local host to connect to aws public key for the instance you are creating. 

![image](https://user-images.githubusercontent.com/97620055/185420114-fe5dd11d-e8a1-4cb0-95cc-76fa325a6b0d.png)

* It should then show the following screen with top line displayed as:

![image](https://user-images.githubusercontent.com/97620055/185422091-ea5f233f-963b-4483-9d4e-93b52d1ae96d.png)

10. To confirm your instance is running on aws you can do see by navigating back to **EC2 dashboard** stated on the top left corner. Naivgate to **instances running** on right of main screen and you shall see the your instance up and running with all status checks done. (2/2 - means 200) 

## Establishing Connection Between Local Host and AWS:  

1. Ensure the **keyname.pem**  key is located in .ssh folder as below and delete from anywhere else as this is **KEY**.

![image](https://user-images.githubusercontent.com/97620055/185424365-ffb43d7a-ee96-4901-8698-9c72a3eb7599.png)

2. Whilst inside .ssh folder, navigate back to where your instance is running and select **connect** on the top bar.

3. Select to SSH client settings and follow the instructions with running relevant command.

![image](https://user-images.githubusercontent.com/97620055/185425433-1cbfab32-97c1-49a0-9a70-b648f398b488.png)

4. To verify your machine will look like on local host once connection is establised between your local host and remote (aws) as below on  your terminal. 

![image](https://user-images.githubusercontent.com/97620055/185426229-a85eb473-f7ee-46e0-8062-7add34552418.png)

## Installing Nodejs & Dependencies:

-  Follow the following commands to install nodjs & dependencies in the Vm terminal:

* Update & Upgrade Ubuntu - OS

sudo apt-get update -y
sudo apt-get upgrade -y

* Install & Enable NGINX

sudo apt-get install nginx -y
sudo systemctl restart nginx
sudo systemctl enable nginx

* Install node.js (version 6.0)
sudo apt install nodejs -y
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

## Data Migration (app folder) to AWS

- In your local host terminal in the home directory, run the following command to copy app folder (or any desired folder) to the remote host:
  
**scp  -i ~/.ssh/eng122.pem -r /c/Users/haide/Sparta_Virtualisation/app  (changes everytime).eu-west-1.compute.amazonaws.com:**

* SCP command (secure copy) - works in similar way to SSH in terms of constructing command (data is secure)
* If process and command configured correctly, this should take few minitues. 
  
## Preparing for App Start Up

1. List all the folders located on virtual terminal 
2. Navigate to the app/app folder
3. Run --> **npm install** if that does not work do **apt-get install npm**.
4. Perform command **npm start** 

## Mongodb Database Setup 

Same configuration as app vm, for security protocol allow port 27017 (private ip app /32).

### Install dependencies on database virtual machine.


- Update & Upgrade Ubuntu - OS : **sudo apt-get update -y --> sudo apt-get upgrade -y**

- Key, Repo, Version Initialised with updates

**sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927**

**echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list**

- Unfinished Updates / Upgrades:  **sudo apt-get update -y --> sudo apt-get upgrade -y**

- Install mondodb

**sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20**

- Mongodb Intialisation: sudo systemctl enable mongod --> **sudo systemctl restart mongod**

- Configure the mongod.conf file with the bind ip as **0.0.0.0** using **sudo nano mongod.conf**

- Restart mongodb with **sudo systemctl restart mongod**

 ### Reconfiguring the App VM

  1. Set the environment variable called **DB_HOST** as: **mongodb://IPv4_db_address/27017/posts**

  2. Run **node seed.js**in seeds directory (inside app folder)

  3. Run **npm start** to start the app.


AWS
ease of use 
flexibiliyu
cost effectiveness
Robustness (Speed)

# AWS - Guidlines & Concepts

*  AWS resources are hosted in multiple locations world-wide. These locations are composed of AWS Regions, Availability Zones, and Local Zones. Each AWS Region is a separate geographic area. Each AWS Region has multiple, isolated locations known as Availability Zones.

## Diagram Displaying Global Structure of AWS:

![image](https://user-images.githubusercontent.com/97620055/185921967-c32f91c3-857e-4e4e-9d7f-a3c8b79dd82a.png)


1. **AWS Regions** - Independent geographical locations spread across globally where data centers reside. Currently has **26 Regions**.
   
2. **Availability Zones** - Within each region there is a **minimum of 2 availability zones**. These are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones
   
3. **Local Zones** - A Local Zone is an extension of an AWS Region that is geographically close to your users. It allows you  place resources, such as compute and storage, in multiple locations closer to your users. Amazon RDS enables you to place resources, such as DB instances, and data in multiple locations. Resources aren't replicated across AWS Regions unless you do so specifically.

* It is important to remember not all regions have same resoruces; therefore it is vital to first look at the requirment of the client or organisation and then recommend what regions would be viable to use. This is restriction is only because some sites can accomodate for more resources then others. 

## The Four Key Pillars of Cloud Computing:

1. **Cost Effectiveness**: AWS allows you to trade fixed expenses (such as data centers and physical servers) for variable expenses, and only pay for IT as you consume it. Plus, the variable expenses are much lower than what you would pay to do it yourself because of the economies of scale.
2. **Agility (Robustness)**: AWS has a broad range of technologies so that you can innovate faster and build nearly anything that you can imagine. You can quickly spin up resources as you need them–from infrastructure services, such as compute, storage, and databases, to Internet of Things, machine learning, data lakes and analytics, and much more.
3. **Elasticity**: Cloud computing allows you to provision as per business activity. You can scale these resources up or down to instantly grow and shrink capacity as your business needs change.
4. **Global Deployment**: With the cloud, you can expand to new geographic regions and deploy globally in minutes. For example, AWS has infrastructure all over the world, so you can deploy your application in multiple physical locations with just a few clicks. Putting applications in closer proximity to end users reduces latency and improves their experience.

## Automate Scripting In AWS Using User Input:

1. Follow steps to create an EC2 instance as described above.
2. Once the configuring instance details reached. Scroll to the bottom and under Advance Details.
3. Selection option of 'text. In the field construct the script starting with **#!/bin/bash**. 

4. Launch the EC2 instance as per commands above. It will take longer to intialise this machine due automatating commands. Hence, will look at load balancing later.
5. To verify script has been automated correctly; use the public ip of the instance and open this on a browser. In this case study, I saw the welcome to nginx page.
6. To make amendments to scrips, stop the instance running, and navigate to instance settings and edit user input. Here, you can modify user input with new commands and then the Vm will spin up with a new set of instructions on cloud.

# The Journey So Far ...

![Image](https://user-images.githubusercontent.com/97620055/185966164-196c4036-6e26-4fa2-8b46-2018d4bf67e9.PNG)

   
## AWS - AMI Creation for App/DB

1. Select the running instance which has been configured with automation via user input.
2. On top right corner, select action, then under image and templates select create image. The screen below should populate.

![image](https://user-images.githubusercontent.com/97620055/185965822-9ad9aa99-baf0-4120-878c-77cc555cee36.png)

![create image](https://user-images.githubusercontent.com/97620055/185965974-9e6504fc-adce-4251-8cc5-a3304c4e2b70.PNG)


3. Enter the name using same naming convention as the instance as well as the a description to allow ease of identification or in real projects same AMI's may be used many times. Recommended to have two versions one stable and one working in case things go wrong you can roll back.  

4. Click creat image and navigate to back to **Images** option on left bar and under AMI, search your ami id that you have created and it show as available. As Below:

![image](https://user-images.githubusercontent.com/97620055/185966347-070e2765-bcbf-488d-9508-21d67ab49c73.png)


## Disaster Recovery Plan (DRP):

- DRP Plan Disaster recovery (DR) is the process that goes into preparing for and recovering from a disaster. This disaster could take one of a number of forms, but they all end up in the same result: the prevention of a system from functioning as it normally does, preventing a business from completing its daily objectives.

### Diagram modelling Amazon S3: 

![image](https://user-images.githubusercontent.com/97620055/186161966-84eae804-ed33-43d7-b128-68f7cd847050.png)


## Amazon S3 Set Up

### Prerequistes Needed

- Pip3 must be installed --> sudo apt install python3-pip  (after checking for version with command **python --version**)
- Python Version 3.7 -> sudo apt-get install python -y  if version still showing set up alias python environment using **alias python=python3**
- AWS Command Line Interface - sudo pip3 install awscli
- AWS Access & Secret Key configurations --> **aws configure** * set region config: **eu-west-1** and output formant: **json**

For the steps below I have used the documentation from link to create python scripts
![https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html?highlight=copy#S3.Client.copy]

## Creation of S3 Bucket



## Uploading Content/File



## Retrieving Content/File



## Deleting Content/File






