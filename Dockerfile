FROM python:3.9

WORKDIR /flask-hotdog

RUN apt-get update

COPY requirements.txt /
RUN pip3 install pip --upgrade \
 && pip3 install -r /requirements.txt 