FROM python:3.8-slim

COPY ./main.py /opt/app/

ENTRYPOINT ["python", "/opt/app/main.py"]