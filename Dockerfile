FROM python:3.10.3
ENV PYTHONUNBUFFERED 1
RUN mkdir blog/
COPY blog /blog/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /blog