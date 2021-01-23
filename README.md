# Arkhn DevOps exercise
Author : **SANOU Abou**

## Step 1

We did a small function. This function is inspired from [here](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/).

In addition, I created a small test file to check if my function is right done.

## Step 2

I create a Dockerfile visible on root folder, this dockerfile will build the docker image to encapsulate the solver part.


```dockerfile
FROM python:3.8
ADD my_solution.py .
ADD checker.py .
ENV RUN_IN_DOCKER Yes
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ENTRYPOINT [ "python3", "./my_solution.py"]
```

The var "RUN_IN_DOCKER" allowed me to check if the code is running in docker (container) or in real computer, in order to choose the

right address. ("localhost:5000" in real computer, or "server:5000" in the container) 

I created another Dockerfile to create the server part image.

To test the my_solution let'try the following command from the root of the project.
```shell script
docker build -t solver .
docker run solver "[({})]"
```

To check the server in container you must move in generator-server folder and run the following line
```shell script
docker build -t server .
docker run server
```


In bonus :-), I made a Docker-compose file to launch multiple containers( server_web and solver)

```shell script
docker-compose up
```

## Step 3

Using a CI to build a publish your docker image.
I uses Github Action.

I created github secrets with docker hub credentials 
I create event on push and pull request.

This event will test the code and pull docker image on docker hub

## Step 4


## Explaining of the Ansible automation part
First, I installed Vagrant and the additional plugin `vagrant-disksize`

* I create a pub key on my own computer in order to connect easy to the VM(ubuntu) 
* I launched the ubuntu VM on vagrant with following command:
```shell script
vagrant up
```
* To connect to the Vm :
```shell script
vagrant ssh
```
in order to automate the process of installation from my own computr to the VM, I did the following steps.
* The file inventory contains the address of different hosts of the solution (In my case the IP of VM or IP of my remote server).
* The file playbook contains the list of runs to do in order to install the docker tool, pull my image and run it with the sample 
of the text to check. 
* from my own computer I launched with the following command:
```shell script
ansible-playbook playbook.yml -i inventory.yml --user vagrant 
```

**--user vagrant** because the default user ot the VM is vagrant in my case.
* I also create a AWS EC2 to deploy the solution. 
To test it, I added the key timesaver.pem in the project, you can run. 
I will remove the server in one week. (So if you check after one week, the server will be unreachable)
```shell script
ansible-playbook playbook.yml -i inventory.yml --user ubuntu --key-file timesaver.pem
```

To check  wih my remote VM.
Let go to the folder "ansible" of the project and run the previous command.

  
