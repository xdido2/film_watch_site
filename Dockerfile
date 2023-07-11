FROM python:3.11.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev


RUN mkdir -p /app
WORKDIR /app

COPY . /app
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/requirements.txt


RUN celery -A root beat -l INFO
RUN celery -A root.celery -l INFO
RUN celery -A root flower
