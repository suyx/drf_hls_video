FROM python:3.9

RUN apt-get update && apt-get install -y \
    ffmpeg

RUN pip install pip --upgrade

RUN mkdir /code

ADD requirements.txt ./

RUN pip install -r requirements.txt

ADD ./ /code/

WORKDIR /code
