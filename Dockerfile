FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /webapp
WORKDIR /webapp
COPY requirements.txt /webapp/
RUN pip install -r requirements.txt
COPY corp /webapp/
