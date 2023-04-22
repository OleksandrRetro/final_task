# Dockerfile

FROM python:3.8.8

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install pip --upgrade &&  pip install -r requirements.txt

COPY *.py /usr/src/app/
