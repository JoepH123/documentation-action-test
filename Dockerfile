FROM python:3.8-slim-buster
LABEL maintainer="Daniel Kapitan <d.kapitan@tue.nl>"

RUN apt-get update
RUN apt-get install nano

RUN mkdir wd
WORKDIR wd
COPY /requirements.txt .
RUN pip3 install -r requirements.txt

COPY / ./

CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "app:server"]