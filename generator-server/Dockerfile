FROM python:3.8
ADD src/server.py .
COPY src/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "./server.py"]
