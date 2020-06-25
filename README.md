# <div align="center"> Under Guidence of </div>
# <div align="center"> ░V░i░m░a░l░ ░D░a░g░a░ </div><br>
### End to End Automation using Kubernetes
#### Task Description
 - Create container image that’s has Linux  and other basic configuration required to run Slave for Jenkins. ( example here we require kubectl to be configured )
 - When we launch the job it should automatically starts job on slave based on the label provided for dynamic approach.
 - Create a job chain of job1 & job2 using build pipeline plugin in Jenkins 
 - Job1 : Pull the Github repo automatically when some developers push repo to Github and perform the following operations as:
    1.  Create the new image dynamically for the application and copy the application code into that corresponding docker image
    2.  Push that image to the docker hub (Public repository) 
 ( Github code contain the application code and Dockerfile to create a new image )
 - Job2 ( Should be run on the dynamic slave of Jenkins configured with Kubernetes kubectl command): Launch the application on the top of Kubernetes cluster performing following operations:
    1.  If launching first time then create a deployment of the pod using the image created in the previous job. Else if deployment already exists then do rollout of the existing pod making zero downtime  for the user.
    2. If Application created first time, then Expose the application. Else don’t expose it.

#### >>> ` Job chain of job1 & job2 using Build Pipeline for Monitoring :` <br><br>
<img src="images/Build-pipeline.png"><br><br>
 
- Here I've used `POLL SCM` to perform the task.
- As the developer commits the codes, Jenkins automatically triggers the jobs and do certain tasks.
- I've used certain plugins for jenkins to perform the JOBS : Docker, CloudBees Docker Build and Publish, Build-pipeline<br><br>
### Cloud Configuration :
<img src="images/cloud-config1.1.png"><img src="images/cloud-config1.2.png"><img src="images/cloud-config1.3.png"><br><br>
### Kube-Config file :
<img src="images/kube-config file.png"><br><br>
### JOB_1 : 
#### >>>
```
 Pull the Github repo automatically when some developers push repo to Github and perform the following operations as:
    1.  Create the new image dynamically for the application and copy the application code into that corresponding 
        docker image
    2.  Push that image to the docker hub (Public repository) 
 ( Github code contain the application code and Dockerfile to create a new image )
```
<br><br>
<img src="images/job1.1.png"><img src="images/job1.2.png"><img src="images/job1.3.png"><img src="images/job1.4.png"><br><br>
### JOB_2 : <br>
#### >>> `(Should be run on the dynamic slave of Jenkins configured with Kubernetes kubectl command)`
```
Launch the application on the top of Kubernetes cluster performing following operations:

1. If launching first time then create a deployment of the pod using the image created in the previous job. Else if
   deployment already exists then do rollout of the existing pod making zero downtime  for the user.
2. If Application created first time, then Expose the application. Else don’t expose it.
``` 
<br><br>
<img src="images/job2.1.png"><img src="images/job2.2.png"><img src="images/rollout-deployment.png"><br><br>
### Web Page :
<img src="images/web-page.png"><br><br>

## Docker_Hub Link : https://hub.docker.com/r/manglam240/kube-ssh


##### Thank You Vimal Sir for this Intresting Task
