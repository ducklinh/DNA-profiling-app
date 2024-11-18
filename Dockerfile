# syntax=docker/dockerfile:1

FROM python:3.12.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD uvicorn api:app --host=0.0.0.0 --port=8000