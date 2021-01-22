FROM python:3.8
MAINTAINER abouopensource
ADD src/server.py .
ENV RUN_IN_DOCKER Yes
COPY src/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "./server.py"]
