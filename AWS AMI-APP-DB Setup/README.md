# AWS - AMI Creation for App/DB

1. Select the running instance which has been configured with automation via user input.
2. On top right corner, select action, then under image and templates select create image. The screen below should populate.

![image](https://user-images.githubusercontent.com/97620055/185965822-9ad9aa99-baf0-4120-878c-77cc555cee36.png)

![create image](https://user-images.githubusercontent.com/97620055/185965974-9e6504fc-adce-4251-8cc5-a3304c4e2b70.PNG)


3. Enter the name using same naming convention as the instance as well as the a description to allow ease of identification or in real projects same AMI's may be used many times. Recommended to have two versions one stable and one working in case things go wrong you can roll back.  

4. Click creat image and navigate to back to **Images** option on left bar and under AMI, search your ami id that you have created and it show as available. As Below:

![image](https://user-images.githubusercontent.com/97620055/185966347-070e2765-bcbf-488d-9508-21d67ab49c73.png)

## Automate Scripting In AWS Using User Input:

1. Follow steps to create an EC2 instance as described above.
2. Once the configuring instance details reached. Scroll to the bottom and under Advance Details.
3. Selection option of 'text. In the field construct the script starting with **#!/bin/bash**. 

4. Launch the EC2 instance as per commands above. It will take longer to intialise this machine due automatating commands. Hence, will look at load balancing later.
5. To verify script has been automated correctly; use the public ip of the instance and open this on a browser. In this case study, I saw the welcome to nginx page.
6. To make amendments to scrips, stop the instance running, and navigate to instance settings and edit user input. Here, you can modify user input with new commands and then the Vm will spin up with a new set of instructions on cloud.