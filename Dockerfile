FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip3 install -r requirements.txt

COPY . .
