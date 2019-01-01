# file to create a container for Django
FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /project

WORKDIR /project

COPY . .
#ADD ./requirements.txt /project/

RUN pip install -r requirements.txt



EXPOSE 8000
