# Week 0 — Billing and Architecture

Before the bootcamp, I had already registered a domain and created a hosted zone using Amazon Route53 on my main AWS account. Follow this [documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)

Once you log into your [Student portal](https://student.cloudprojectbootcamp.com/users/sign_in), From the Resources section, you watch all the [Video Instructional Content Playlist](https://www.youtube.com/watch?v=8b8SvQHc4Pk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv) 

- You can also watch the same, Click on Submissions, Week 0, From the ToDo List. 
- ***Proceed with setting up the following tasks that you need for this bootcamp as per the instructions given in the videos.***
- Update the Checklist

# Required Tasks needed to complete the Homework

## 1. Create a Github Account 

As I already have [my Github Account](https://github.com/awsmine), I did not create a new one.

  * ### 1b. Setup a MFA on my GitHub account for extra security. 

- [Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)

## 2. Create a Free Gitpod Account 

This is used for Cloud Developer Environment (CDE) to work with the code, similar to Cloud9, but without spinning up an EC2 instance.

## 3. I got the Gitpod Button on my Github Account. 

## 4. Create Gitpod Codespaces

I may need them in future, in case the I used up all the Gitpod free-tier.

## 5. Creating Your Repository from the Github Template

From the [Bootcamp website](https://aws.cloudprojectbootcamp.com/), go all the way down to the cloud project - Use [Starting template](https://github.com/ExamProCo/aws-bootcamp-cruddur-2023), Click - `Use this template` button, and select - `Create a new respository` - putting in the exact name - `aws-bootcamp-cruddur-2023`, check - `Public`, and then Click - `Create repository from this template.`

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Create_repository_aws-bootcamp-cruddur-2023.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Create_repository_aws-bootcamp-cruddur-2023.pdf)

Once the repository was created, I could see all of the template folders/files available in the repository.

## 6. Create an AWS Account 

As I already have one, I did not create another Account.

## 7. Create a Free Lucidchart Account to draw AWS Architectural diagrams

## 8. Create a Free Honeycomb.io Account

## 9. Create a Free Rollbar Account

## 10. Install AWS CLI to launch Gitpod environment on the main branch

- Follow [installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

- Expand the section on Linux, and copy and paste the bash commands into `.gitpod.yml` on Gitpod

- On Gitpod, Update `.gitpod.yml` to include the following task 

- Set AWS CLI to use `partial autoprompt` mode to make it easier to debug CLI commands.

- [aws-bootcamp-cruddur-2023/.gitpod.yml](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/.gitpod.yml)

```
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```

- Run `git commit`

- Run `git push`

- If you run into an error doing a `git push`, make sure you have given Gitpod `write permission to public_repo` in your [Github integration](https://gitpod.io/user/integrations)

## 11. Create a new User and Generate AWS Credentials

 - From [IAM Users Console](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users),  login as a root user

- Create an IAM user - `bobby`
- `Enable Console access` for the user
- Create a new `Admin group - admin` and `apply AdminstratorAccess`
- `Create the user`
- `Click on the user`, Click `Security Credentials` and `Create Access Key`
- Choose `Command Line Interface (CLI)`, `Create Access key`
- `Download the CSV with the credentials`

- set environment variables that are needed in the GITPOD

```
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION=us-east-1
```
- Save these environment variable into Gitpod when we relaunch our workspaces

```
gp env AWS_ACCESS_KEY_ID=""
gp env AWS_SECRET_ACCESS_KEY=""
gp env AWS_DEFAULT_REGION=us-east-1
```

- You can also [check the variables]( https://gitpod.io/user/variables) in 

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
```

- Then go to your Github page, click the `Gitpod` button, and it should spin up a new workspace and set up the aws cli with your AWS account info.


### Validate the AWS CLI by checking for user's identity

```
aws sts get-caller-identity
```
 
- shows that you are accessing AWS CLI with the right credentials.

```
{
    "UserId": "XXXXXXXXXXXXXXXXXXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/bobby"
}
```

- You can verify you have the proper info in your environment variables and they are importing properly by running

```
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY
echo $AWS_DEFAULT_REGION
```


## 12. Billing Setup

Billing alerts will notify the user if the AWS usage cost rises above a certain threshold.

### Enable the Billing alert
- To enable it ---> Go to AWS Billing page and `Under Billing Preferences` Choose `Receive Billing Alerts`
- Save Preferences

### Create SNS Topic

- First create SNS topic before we create an alarm.

- This is what alerts you when hit the set threshold of cost.

- [aws sns create-topic](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html)


```
aws sns create-topic --name billing-alarm
```

- This will return a SNS topic ARN.

```
aws sns list-topics
{
    "Topics": [
        {
            "TopicArn": "arn:aws:sns:us-east-1:0274:Billing_alarm"
        }
    ]
}
```

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Billing_alarm_ARN.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Billing_alarm_ARN.pdf)


- Create a SNS subscription and associate the above ARN and the email where you want the alert.

```
aws sns subscribe \
    --topic-arn TopicARN \
    --protocol email \
    --notification-endpoint your@email.com
```

- Check your email and confirm the subscription


### Create the Cloudwatch Alarm

- [aws cloudwatch put-metric-alarm[(https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html)

- [Create an Alarm via AWS CLI](https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-estimatedcharges-alarm/)

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Billing_alarm_ARN.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_setup_Billing_Alarms.pdf)

```
aws cloudwatch put-metric-alarm --cli-input-json file://aws/json/alarm-config.json
```

- [aws-bootcamp-cruddur-2023/aws/json/alarm-config.json](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/aws/json/alarm-config.json)

## 13. Create an AWS Budget

- Create only 1 budget not to go over the free budget limit

- [aws budgets create-budget](https://docs.aws.amazon.com/cli/latest/reference/budgets/create-budget.html)

- Run AWS Cli to extract the AWS Account ID

```
aws sts get-caller-identity --query Account --output text
```

- use the Account ID from the previous command output

- Update the json files with email address


- [aws-bootcamp-cruddur-2023/aws/json/budget.json](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/aws/json/budget.json)

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_setup_Monthly_Budget.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_setup_Monthly_Budget.pdf)

- [aws-bootcamp-cruddur-2023/aws/json/budget-notifications-with-subscribers.json](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/aws/json/budget-notifications-with-subscribers.json)


```
aws budgets create-budget \
    --account-id AccountID \
    --budget file://aws/json/budget.json \
    --notifications-with-subscribers file://aws/json/budget-notifications-with-subscribers.json
```


#  Homework Challenges

## Set MFA, IAM role

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_user_bobby_setup_MFA](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_user_bobby_setup_MFA.pdf)

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Role_S3Full.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Role_S3Full.pdf)

## Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue.

Follow [Monitoring Amazon Health events with Amazon EventBridge](https://docs.amazonaws.cn/en_us/health/latest/ug/cloudwatch-events-health.html)

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Eventbridge_Health-rule-notify-1.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Eventbridge_Health-rule-notify-1.pdf)
- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Eventbridge_EC2_health-2.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Eventbridge_EC2_health-2.pdf)
- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Eventbridge_SNS_topic-3.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Eventbridge_SNS_topic-3.pdf)

## Review all the questions of each pillars in the Well Architected Tool (No specialized lens)

- This is not related to the course, but I thought I should mention this.

- Some time back, in Sept 2022, I completed the training for Well Architected Tool and earned a [Well-Architected Proficient Badge](https://www.credly.com/badges/268d14c8-a150-4b3c-8e23-1ac3823abae0/linked_in)

- Created a workload **week_0_project** to do this task in getting the report for my project using the **Logical CI/CD pipeline Diagram**

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Well_Architeched_Tool_report.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Well_Architeched_Tool_report.pdf)


## Create an architectural diagram (to the best of your ability) the CI/CD logical pipeline in Lucid Charts

### 1. Logical Diagram

Link to my Logical Diagram from Lucid Chart

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Logical_Architectural_Diagram_Lucidchart.png](https://lucid.app/lucidchart/61cf470e-1feb-42c5-afdb-792fb1e4fb85/view?page=0_0&invitationId=inv_4088e3a2-9db3-4c69-951d-5895298985bc#)

- Link to my Logical Diagram PDF file

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Logical diagram.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Logical%20diagram.pdf)

### 2. Coceptual Diagram + Conceptual Diagram on Napkin


- Link to my Conceptual Diagram from Lucid Chart

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Conceptual_Diagram_Lucidchart.png](https://lucid.app/lucidchart/540635e4-8c10-4855-9d62-652763d2a6c1/view?page=0_0&invitationId=inv_02a3c339-9428-4489-a816-8313cbfd28d8#)

- Link to my Conceptual Diagram PDF file

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Conceptual diagram.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Conceptual%20diagram.pdf)

- Link to my Conceptual Diagram on Napkin

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Conceptual_Napkin_diagram.jpg](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Conceptual_Napkin_diagram.jpg)


### 3. Logical CI/CD pipeline Diagram

- Link to my Logical CI/CD Diagram from Lucid Chart

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Logical_CI_CD_diagram_Lucidchart.png](https://lucid.app/lucidchart/3f5a105a-3ee6-4af9-b150-e1fc58b1b895/view?page=0_0&invitationId=inv_89d37443-e0b0-46a7-902d-63f22edd1de3#)

- Link to my Logical CI/CD Diagram PDF file

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Logical_CI_CD diagram.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Logical_CI_CD%20diagram.pdf)

## Research the technical and service limits of specific services and how they could impact the technical path for technical flexibility. 

### Amazon Elastic Compute Cloud (EC2) 

Amazon Elastic Compute Cloud (EC2) is a most commonly and widely used cloud computing service provided by Amazon Web Services (AWS) which provides scalable computing capacity in the cloud. 

- EC2 offers a high degree of technical flexibility and supports a wide variety of use cases.

- But there are some technical and service limits that could impact the technical path for flexibility.

### Technical limits of EC2 that I could think of


- **Instance Limits:** The number of EC2 instances that a user can launch is limited by default, usually 5. These limits can be increased by submitting a request to AWS, which I did today by raising a service ticket. If a user exceeds these limits without increasing them, it can impact the flexibility of their technical path.

- **Instance types:** EC2 offers several instance types with varying amounts of CPU, memory, and storage capacity. Each instance type has a limit on the number of instances that can be launched, and the total number of vCPUs that can be used.

- **Network:** EC2 instances are connected to the internet through Amazon VPC. VPC has limits on the number of subnets, security groups, and network interfaces that can be created.

- **Network Interfaces:** Each EC2 instance can have a limited number of network interfaces. If a user needs to connect their instances to multiple networks or use multiple IP addresses, they may need to use additional instances or consider other AWS services.

- **Storage:** EC2 provides different types of storage options, including Elastic Block Store (EBS), instance store, and Amazon S3. Each storage type has different limits on storage capacity, IOPS, and throughput.


### Sonme service limits of EC2

- **Volumes:** EC2 instances can attach a limited number of volumes, and each volume has a maximum size limit. This can impact the technical path if a user needs to attach more volumes or use larger volumes.

- **Availability Zones:** EC2 instances can be launched in different availability zones (AZs) to improve availability and fault tolerance, which are isolated data centers within a region. There are limits on the number of instances that can be launched in each AZ, and the total number of instances that can be launched in a region.

- **Security:** EC2 provides several security features, including network security groups, IAM roles, and encryption. There are limits on the number of security groups, IAM roles, and keys that can be created.

- **Elastic IP addresses:** EC2 provides elastic IP addresses (EIPs) that can be associated with instances. There are limits on the number of EIPs that can be allocated per account.

- **Auto Scaling:** EC2 Auto Scaling allows users to automatically scale the number of instances based on demand. There are limits on the number of Auto Scaling groups and launch configurations that can be created.

**Amazon Machine Images (AMIs):** EC2 instances can be launched from pre-configured Amazon Machine Images (AMIs). There are limits on the number of AMIs that can be created and shared.

- **Regional limitations:** Some EC2 features may not be available in all AWS regions. For example, certain instance types may only be available in specific regions, and some instance types may have limited availability in certain regions.

These limits can impact the technical path for technical flexibility in several ways. 

**For example**, if a company needs to launch a large number of instances, they may need to select an instance type that has a high number of vCPUs, and use multiple availability zones to distribute the load. 

**For example**, if a company needs to store large amounts of data, they may need to use multiple storage types, such as EBS and S3, to accommodate the data. 

**For example**, if a company needs to launch instances in multiple regions, they may need to allocate EIPs across regions to ensure seamless connectivity.

To address these limits, companies can work with AWS support to increase their limits or consider using other AWS services, such as EC2 Spot Instances or Amazon Elastic Kubernetes Service (EKS), to optimize their infrastructure.

Additionally, if a customer requires certain instance types that are only available in certain regions, they may need to choose a different region or use a different service altogether. These limitations can also impact application architecture and design, as well as the overall cost of running applications on EC2.

In conclusion, EC2 provides a highly flexible and scalable infrastructure for running various types of workloads, but its technical and service limits can impact the technical path for flexibility. It is essential to understand these limits and plan accordingly to achieve maximum technical flexibility.

### Application Load Balancer (ALB)




## Open a support ticket and request a service limit

Follow [Request a Quota Increase with Service Quotas](https://aws.amazon.com/getting-started/hands-on/request-service-quota-increase/)

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Service_Quota_incr_EC2_50.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Service_Quota_incr_EC2_50.pdf)

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Service_Quota_incr_Pending.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Service_Quota_incr_Pending.pdf)

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Service_Quota_incr_EC2_50_Support_ticket.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Service_Quota_incr_EC2_50_Support_ticket.pdf)

- [aws-bootcamp-cruddur-2023/journal/assets/week_0_Service_Quota_incr_Resolved.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Service_Quota_incr_Resolved.pdf)







## Cloud Technical Essays

- [Challenges facing during AWS Cloud Project Bootcamp by Andrew Brown](https://dev.to/aws-builders/challenges-facing-during-aws-cloud-project-bootcamp-by-andrew-brown-52ee)

- [Getting the serverless cache icon for AWS Cloud Project Bootcamp by Andrew Brown](https://dev.to/aws-builders/getting-the-serverless-cache-icon-for-aws-cloud-project-bootcamp-by-andrew-brown-4poi)


## Knowledge Challenges

- Security Quiz - Submitted

- Pricing Quiz - Submitted



