FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    bash \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/bash", "/code/_CI/entrypoint.sh"]