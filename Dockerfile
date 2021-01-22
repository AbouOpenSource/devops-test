FROM python:3.8
ADD my_solution.py .
ADD checker.py .
ENV RUN_IN_DOCKER Yes
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ENTRYPOINT [ "python3", "./my_solution.py"]
