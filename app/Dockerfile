FROM python:3.8.5-alpine

COPY ./requirements.txt /app/requirements.txt

COPY templates /app/templates

COPY . /app

EXPOSE 5000

WORKDIR /app


RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD python3 app.py