# AWS - Guidlines & Concepts

## AWS - Best Practices To Implement: 
 - Naming convention eng_122_haider_ec2
 - AWS services to be used between 09:00 - 18:00 stop or terminate
 - If your need to use it out of hours please ask
 - WE MUST ONLY USE IRELAND.
 - terminate services once you finished working. 
 - Do not delete anyone else's services
 - MUST NOT SHARE AWS ACCOUNT DETAILS WITH ANYONE - SO NO GITHUB REPO

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