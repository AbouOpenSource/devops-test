# Arkhn DevOps exercise
Author : **SANOU Abou**

## Step 1

We did a small function. This function is inspired from [here](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/).

In addition, I created a small test file to chekc if my function is right done.

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

## Step 3

Using a CI to build a publish your docker image.
I uses Github Action.

I created github secrets with docker hub credentials 
