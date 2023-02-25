# Week 1 — App Containerization


For week1, I have decided not to put the code for the tasks, but write down and document how I completed all the tasks watching Andrew's Videos 2-3x.

- I wrote down the code for each task on the notepad, and went over the videos again to check and then executed them.
 
- The instructions were so clear and perfect!

# Before starting Homework Challenges

- For week 1 App Containerization, Watched videos from [FREE AWS Cloud Project Bootcamp](https://www.youtube.com/watch?v=8b8SvQHc4Pk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=1)

- And followed the instructions from https://github.com/omenking/aws-bootcamp-cruddur-2023/blob/week-1/journal/week1.md to do the tasks for Containerize Backend and Frontend Flasks, Multiple Containers and Adding DynamoDB Local and Postgres.

- For creating DynamoDB table, I followed [Challenge Dynamodb Local](https://github.com/100DaysOfCloud/challenge-dynamodb-local)

- For adding Notifications to the Front End Flask, followed instructions from Andrew's videos.

- While doing the tasks, made sure to open the ports as and when neccessary.

- Commit the changes made to the files as soon as they ran well to give the desired output and there are no errors.

- If you get error while committing the changes to GitHub, you have to pull, merge and then push them to GitHub

```
git pull

# merge
git config pull.rebase true

git push
```

- Take photos of the tasks completed and uploaded them to the [aws-bootcamp-cruddur-2023/_docs/assets/week_1/](https://github.com/awsmine/aws-bootcamp-cruddur-2023/tree/main/_docs/assets/week_1)

- Remember to cleanup the resources that you have created

```
docker rmi -f <REPOSITORY:TAG NAME>

docker rmi -f <IMAGE ID>

docker stop <CONTAINER NAME>

docker rm <CONTAINER NAME>
```

- After spinning up your workspace, you have to run ***npm Install*** before building the container, so that it can copy the contents of node_modules.

- This is needed to get the app to run locally every time you spin up your workspace in Gitpod

```
cd frontend-react-js

npm i
```


## Images for Front and Back Ends

- [frontend-flask-working.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/frontend-flask-working.pdf)

- [frontend-flask-cloud-is-fun-mesg.png](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/frontend-flask-cloud-is-fun-mesg.png)

- [frontend-flask-cloud-is-very-fun-mesg.png](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/frontend-flask-cloud-is-very-fun-mesg.png)

## Images for DynamoDB and Postgres

- [dynamo-db-list-table-Music.jpg](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/dynamo-db-list-table-Music.jpg)

- [dynamo-db-scan-table-Music.png](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/dynamo-db-scan-table-Music.png)

- [postgres-db.jpg](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/postgres-db.jpg)

## Images for Notifications

- [add-notifications-empty-error.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/add-notifications-empty-error.pdf)

- [add-notifications-get-method-to-openapi.jpg](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/add-notifications-get-method-to-openapi.jpg)

- [add-notifications-file-to-get-my-own-data.jpg](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/add-notifications-file-to-get-my-own-data.jpg)

- [add-notifications-to-get-my-own-data.jpg](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/add-notifications-to-get-my-own-data.jpg)




# Homework Challenges

## 1. Run the dockerfile CMD as an external script

- Login to Cloud9 IDE `


```
mkdir app
```

- Create app.py

```
#!/usr/bin/env python3.7

print ("Hello World")
```

- Create Dockerfile

```
FROM python:3.8-alpine 

COPY . /app 

WORKDIR /app 

CMD ["python","app.py"] 
```

- Run the command to build image 

```
docker build -t helloworld . 
```

- Image for [HW-1-Run the dockerfile CMD as an external script.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-1-Run%20the%20dockerfile%20CMD%20as%20an%20external%20script.pdf)

- Image for [HM-1-Remove the images.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HM-1-Remove%20the%20images.pdf)


## 2. Push and tag a image to DockerHub (they have a free tier)

- Login to Cloud9 IDE `

**1. pull latest image of Centos**

```
docker pull centos:latest
docker images
```

- [HW-2-pull-centos.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-2-pull-centos.pdf)


**2. Installing Apache web server through Dockerfile and index.html**

- Dockerfile

```
# defines the container where we want to run all the projects.
FROM centos:latest

# maintaining the container
MAINTAINER Joshi
RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

# updating the neccessary packages
RUN yum -y update

# installing apache web server
RUN yum -y install httpd

# copying the index.html
COPY index.html /var/www/html/

# httpd service status must be ON every time.
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

# exposing port 80
EXPOSE 80
```

- index.html

```
<html>
    <body>
        <h1> Welcome, this is an Customized Docker image on an Apache Web server </h1>
    </body>
</html>
```

**3. login to docker hub, put your password, after login succeeded**

```
docker login -u <DOCKERHUB USERNAME>
```


**4. tag the original image**

```
docker tag centos:latest <DOCKERHUB USERNAME>/<REPO name — create your own:TAG NAME>
docker tag centos:latest <DOCKERHUB USERNAME>/centosrev:latest
```

**5. build your image with the VERSION build argument that is set to 1.5, build the image centosrev - with a tag 1.5**

```
docker build -t <DOCKERHUB USERNAME>/<REPO name — create your own:TAG NAME> .
docker build -t <DOCKERHUB USERNAME>/centosrev:1.5 .
```

```
docker images
```

- [HW-2-Tag-Images-v1.5.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-2-Tag-Images-v1.5.pdf)



**6. push the original tagged and v1.5 images into DockerHub**


```
docker push <DOCKERHUB USERNAME>/<REPO:TAG NAME>
	
docker push <DOCKERHUB USERNAME>/centosrev:latest
docker push <DOCKERHUB USERNAME>/centosrev:v1.5
```

- [HW-2-Pushed v1.5 into DockerHub.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-2-Pushed%20v1.5%20into%20DockerHub.pdf)

**7. Deleting the Docker Hub credentials from the ~/.docker/config.json**

```
docker logout
```


 
## 3. Use multi-stage building for a Dockerfile build

- Containers are made of layers. Compile and install operations performed in the image, add to the layers, increasing the size of the container. Instead of keeping all of those layers into the final image, you can split those steps off, and only use the finished product. Docker provides this capability through multi-stage builds. In this lab, you will build an image the usual way, and inspect the image to see how it is put together. You'll then convert the Dockerfile to use multi-stage builds, and see how the new image compares.

### Stage 1 - Build the application

- Login to Cloud9

```
mkdir singlestage
cd singlestage
```

- helloworld.go
```
package main

import "fmt"

func main() {
	fmt.Println("hello world")
}
```

- Dockerfile

```
FROM golang:1.13.1
WORKDIR /tmp
COPY helloworld.go .
RUN GOOS=linux go build -a -installsuffix cgo -o helloworld .
CMD ["./helloworld"]
```
- Build the image

```
docker build -t single-stage .
docker images

# Set a variable to show the size of the image:
export showSize='{{ .Size }}'

# Show the size of the image:
docker inspect -f "$showSize" single-stage | numfmt --to=iec
```

- Check **docker image of 777MB**

- [HW-3-Single-Stage-Image.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-3-Single-Stage-Image.pdf)


### Stage 2: Create the final small image

```
# from the root directory
mkdir multistage
cd multistage/
```

- Copy the helloworld program here
```
$ cp ../single-stage/helloworld.go .
```

- Dockerfile

```
FROM golang:1.13.1 as multistage
WORKDIR /tmp
COPY helloworld.go .
RUN GOOS=linux go build -a -installsuffix cgo -o helloworld .
CMD ["./helloworld"]

FROM alpine:3.10.2
WORKDIR /root
COPY --from=multistage /tmp/helloworld .
CMD ["./helloworld"]
```

- Build the smaller image

```
 docker build -t multi-stage .
 docker images

# Set a variable to show the size of the image:
export showSize='{{ .Size }}'

# Show the size of the image:
docker inspect -f "$showSize" single-stage | numfmt --to=iec
```

- As you can see using multi-stage build, we can significantly reduce the size of the image.

- **It is 7.3MB**

- [HW-3-Multi-Stage-Image.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-3-Multi-Stage-Image.pdf)


## 4. Implement a healthcheck 

- Docker allows us to tell the platform on how to test that our application is healthy.

- When Docker starts a container, it monitors the process that the container runs. 

- If the process ends, the container exits. 

- We can specify certain **options** before the CMD operation, these includes:

```
HEALTHCHECK --interval=5s CMD ping -c 1 172.17.0.2

--interval=DURATION (default: 30s)
--timeout=DURATION (default: 30s)
--start-period=DURATION (default: 0s)
--retries=N (default: 3)
```

**References**

- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

- [HEALTHCHECK](https://docs.docker.com/engine/reference/run/#healthcheck)


**1. launch a container from a busybox image**

```
docker container run -dt --name busybox busybox sh

# check container is up and running
docker ps
```



**2. get the ip address of the busybox container**

```
docker inspect busybox 
```

- running for 5s

- [HW-4-get-IP-busybox-container.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-4-get-IP-busybox-container.pdf)


**3. Create a Dockerfile**

```
FROM busybox
HEALTHCHECK --interval=5s CMD ping -c 1 172.17.0.2
```

**4. build the container**

```
docker build -t monitoring .

dpocker images
```

**5. launch a container from the monitoring image**

```
docker run -dt --name monitor monitoring sh
```


- docker ps to see the healthcheck

- depending upon the interval you specify the healthcheck would be perfomon accordings

- it is healthy because it is able to ping the busybox container

- [HW-4-healthy.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-4-healthy.pdf)

**6. docker inspect monitor to see the healthy exitcode 0**

- [HW-4-inspect-busybox.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-4-inspect-busybox.pdf)

**7. healthy exitcode 0**

- [HW-4-healthy-exitcode-0.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-4-healthy-exitcode-0.pdf)

**8. docker stop busybox, Docker Container becomes unhealthy**

```
docker ps
```

- unhealthy

- [HW-4-busybox-stop-container-monitor-unhealthy.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-4-busybox-stop-container-monitor-unhealthy.pdf)


**9. specify interval=5s and retries=1**

```
docker run -dt --name tmp --health-cmd "curl -f http://localhost" --health-interval=5s --health-retries=1 busybox sh
```

- [HW-4-retries-1.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-4-retries-1.pdf)
- 

**10. Clean Up**

- docker stop CONTAINER NAME

- docker rm CONTAINER NAME
	
- docker rmi -f REPOSITORY:TAG NAME

- docker rmi -f IMAGE ID
	
	

## 5. Research best practices of Dockerfiles and attempt to implement it in your Dockerfile

**1.** Use a small base image: Start with a small base image such as Alpine, as it has a smaller attack surface and reduces the size of your Docker image.

**2.** Reduce the number of layers: Minimize the number of layers in your Docker image by combining multiple RUN commands into one, using multi-stage builds, and removing unnecessary files after each step.

**3.** Use caching effectively: Leverage Docker's caching mechanism by placing the most frequently changed commands at the end of the Dockerfile and using the --no-cache flag when necessary.

**4.** Use specific tags: Always use specific tags for your base image and any other images you pull from Docker Hub to ensure reproducibility and avoid unexpected updates.

**5.** Use environment variables: Use environment variables instead of hardcoding values in your Dockerfile to make your images more flexible and configurable.

**6.** Remove unnecessary files: Remove any temporary files and other artifacts that are not needed in the final image to keep the image size small.

**7.** Avoid running processes as root: Avoid running processes in your Docker container as the root user, as this can lead to security vulnerabilities. Instead, create a new user in the Dockerfile and run processes as that user.

**8.** Use labels: Use labels to provide metadata about your Docker image, such as version, author, and description.


**Here's an example Dockerfile that follows these best practices:**

```
bash
Copy code
# Use a small base image
FROM alpine:3.14.2

# Set environment variables
ENV APP_HOME=/app \
    APP_USER=myuser

# Create a new user
RUN adduser -D -h ${APP_HOME} ${APP_USER}

# Install necessary packages
RUN apk --update --no-cache add \
    python3 \
    py3-pip \
    && pip3 install --no-cache-dir --upgrade pip

# Copy application files
WORKDIR ${APP_HOME}
COPY requirements.txt ${APP_HOME}
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . ${APP_HOME}

# Remove unnecessary files
RUN rm -rf .git \
    && rm -rf __pycache__

# Change ownership to the new user
RUN chown -R ${APP_USER}:${APP_USER} ${APP_HOME}

# Switch to the new user
USER ${APP_USER}

# Specify metadata
LABEL version="1.0" \
      author="John Doe" \
      description="My Dockerized app"

# Start the application
CMD ["python3", "app.py"]
```



- This Dockerfile uses Alpine as a base image, installs necessary packages, and copies the application files. 

- It also creates a new user, removes unnecessary files, and uses labels to provide metadata.

-  Finally, it starts the application process as a non-root user. 
 
-  By following these best practices, you can create secure, efficient, and maintainable Docker images.


## 6. Learn how to install Docker on your local machine and get the containers running outside of Gitpod / Codespaces

- I could not install Docker on my local machine, so I worked on Cloud9 to install EC2 instance.

- Wrote an article about this [week 1- Challenges facing during AWS Cloud Project Bootcamp by Andrew Brown](https://dev.to/aws-builders/week-1-challenges-facing-during-aws-cloud-project-bootcamp-by-andrew-brown-4e05)

- Login to Cloud9

**1. launch an EC2 instance , t2 micro, with a Keypair, security group to allow SSH traffic on port 22, as well as HTTP traffic on port 80**

```
sudo su
yum update -y
yum install docker -y 
systemctl enable docker.service
systemctl start docker.service
systemctl status docker.service
```

**2. Pull a centos image**

```
docker pull centos:latest
docker images
```

- [HW-6-install-Docker-on-ec2-instance.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-6-install-Docker-on-ec2-instance.pdf)



**3. launch a container from the monitoring image**

```
docker run -dt --name centosrev centos sh
```

- [HW-6-centosrev-container.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-6-centosrev-container.pdf)


## 7. Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes.


- Checked the AMI Marketplace for an image with Docker already installed.
- Selected the Amazon ECS-Optimized Amazon Linux 2 (AL2) x86_64 AMI image - AMI ID# ami-05e7fa5a3b6085a75.
- Used a t2.micro instance free-tier, with a Keypair to access EC2.
- Created a security group to allow SSH traffic on port 22, and HTTP on Port 80

```
[ec2-user@ip-172-31-8-30 ~]$ docker --version
Docker version 20.10.17, build 100c701
```

**2. Pull a centos image**


```
[ec2-user@ip-172-31-8-30 ~]$ docker pull centos
Using default tag: latest
latest: Pulling from library/centos
a1d0c7532777: Pull complete
Digest: sha256:a27fd8080b517143cbbbab9dfb7c8571c40d67d534bbdee55bd6c473f432b177
Status: Downloaded newer image for centos:latest
docker.io/library/centos:latest
```

**3. Check the images**

```
[ec2-user@ip-172-31-8-30 ~]$ docker image ls
REPOSITORY                  TAG            IMAGE ID       CREATED         SIZE
amazon/amazon-ecs-agent     latest         7149da18e4f3   7 weeks ago     68MB
ecs-service-connect-agent   interface-v1   606b6b4c0b10   4 months ago    115MB
centos                      latest         5d0da3dc9764   17 months ago   231MB
amazon/amazon-ecs-pause     0.1.0          9dd4685d3644   8 years ago     702kB

```

**4. launch a container from the centos image**

```
docker run -dt --name centos-docker centos sh
```

- [HW-7-ec2-docker-container.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_1/HW-7-ec2-docker-container.pdf)




# Knowledge Challenges

- Security Quiz - Submitted

- Pricing Quiz - Submitted


# Cloud Technical Essays

- [week 1- Challenges facing during AWS Cloud Project Bootcamp by Andrew Brown](https://dev.to/aws-builders/week-1-challenges-facing-during-aws-cloud-project-bootcamp-by-andrew-brown-4e05)

- [Implementing a healthcheck for a Docker Container](https://dev.to/aws-builders/implementing-a-healthcheck-for-a-docker-container-4m9h)

