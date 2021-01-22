FROM python:3.8
MAINTAINER abouopensource
ADD src/server.py .
COPY src/requirements.txt ./requirements.txt
RUN pip install -r app/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "./server.py"]
