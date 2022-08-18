# Cloud Computing

## AWS - Best Practices To Implement: 
 - Naming convention eng_122_haider_ec2
 - AWS services to be used between 09:00 - 18:00 stop or terminate
 - If your need to use it out of hours please ask
 - WE MUST ONLY USE IRELAND.
 - terminate services once you finished working. 
 - Do not delete anyone else's services
 - MUST NOT SHARE AWS ACCOUNT DETAILS WITH ANYONE - SO NO GITHUB REPO 
 
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

- In your local host terminal run the following command to copy app folder (or any desired folder) to the remote host
**scp  -i ~/.ssh/eng122.pem -r /c/Users/haide/Sparta_Virtualisation/app  ubuntu@ec2-52-209-212-251.eu-west-1.compute.amazonaws.com:**
* If process and command configured correctly, this should take few minitues. 
  
## Preparing for App Start Up
1. List all the folders located on virtual terminal 
2. Navigate to the app/app folder
3. Run --> **npm install** if that does not work do **apt-get install npm**.
4. Perform command **npm start** 




