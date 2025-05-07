FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
RUN apk update && apk upgrade && \
    apk add --no-cache bash

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["/bin/bash", "/code/_CI/entrypoint.sh"]