FROM python:3.11
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y && apt install nano -y
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt