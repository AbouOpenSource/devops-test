FROM python:3.8
ADD src/server.py .
COPY src/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ENTRYPOINT [ "python3", "./server.py"]
