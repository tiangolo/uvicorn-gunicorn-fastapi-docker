FROM tiangolo/uvicorn-gunicorn:python3.9

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install --no-cache-dir fastapi

COPY ./app /app
