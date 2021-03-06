FROM python:3.7-stretch

ENV PYTHONWARNINGS ignore

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -Ur requirements.txt --quiet

WORKDIR /webapps

EXPOSE 5000
