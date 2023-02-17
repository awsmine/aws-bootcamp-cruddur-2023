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
[aws-bootcamp-cruddur-2023/journal/assets/week_0_user_bobby_setup_MFA](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_user_bobby_setup_MFA.pdf)

## 2. Create a Free Gitpod Account 

This is used for Cloud Developer Environment (CDE) to work with the code, similar to Cloud9, but without spinning up an EC2 instance.

## 3. I got the Gitpod Button on my Github Account. 

## 4. Create Gitpod Codespaces

I may need them in future, in case the I used up all the Gitpod free-tier.

## 5. Creating Your Repository from the Github Template

From the [Bootcamp website](https://aws.cloudprojectbootcamp.com/), go all the way down to the cloud project - Use [Starting template](https://github.com/ExamProCo/aws-bootcamp-cruddur-2023), Click - `Use this template` button, and select - `Create a new respository` - putting in the exact name - `aws-bootcamp-cruddur-2023`, check - `Public`, and then Click - `Create repository from this template.`

[aws-bootcamp-cruddur-2023/journal/assets/week_0_Create_repository_aws-bootcamp-cruddur-2023.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_Create_repository_aws-bootcamp-cruddur-2023.pdf)

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

[aws-bootcamp-cruddur-2023/.gitpod.yml](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/.gitpod.yml)

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

[aws-bootcamp-cruddur-2023/journal/assets/week_0_Billing_alarm_ARN.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_setup_Billing_Alarms.pdf)

```
aws cloudwatch put-metric-alarm --cli-input-json file://aws/json/alarm-config.json
```

- [larm-config.json](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/aws/json/alarm-config.json)


























=======================================
# Week 0 Viewing material

Once you log into your Student portal - https://student.cloudprojectbootcamp.com/users/sign_in, Click on Submissions, Week 0, From the ToDo List, you watch all the Video Instructional Content Playlist - https://www.youtube.com/watch?v=8b8SvQHc4Pk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv. Proceed with setting up of things that you need for this bootcamp as per the instructions given in the videos.

# Required Homework/Tasks

**1.** Create a Github Account 
- I did not create a new Github Account, as I already have one, https://github.com/awsmine

 1b. I setup a MFA on my GitHub account for extra security. PDF in week_0 folder.

PDF file - https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week_0_user_bobby_setup_MFA.pdf


2. Create a Free Gitpod Account which is used for Cloud Developer Environment (CDE) to work with the code.

3. I got the Gitpod Button on my Github Account. 

4. Create Gitpod Codespaces, in case the I used up all the Gitpod free-tier.




# Architecture Diagram

Here is the link to my Logical Diagram from Lucid Chart
https://lucid.app/lucidchart/61cf470e-1feb-42c5-afdb-792fb1e4fb85/view?page=0_0&invitationId=inv_4088e3a2-9db3-4c69-951d-5895298985bc#

Here is my Conceptual Diagram from Luci Chart
https://lucid.app/lucidchart/540635e4-8c10-4855-9d62-652763d2a6c1/view?page=0_0&invitationId=inv_02a3c339-9428-4489-a816-8313cbfd28d8#

Here is link to my Logical CI/CD Diagram from Lucid Chart
https://lucid.app/lucidchart/3f5a105a-3ee6-4af9-b150-e1fc58b1b895/view?page=0_0&invitationId=inv_89d37443-e0b0-46a7-902d-63f22edd1de3#



