FROM python:3.6.9-alpine

RUN apk add --no-cache mariadb-dev build-base
RUN apk add --no-cache tzdata
ENV TZ America/Los_Angeles

RUN mkdir -p /var/www/steem-tools
WORKDIR /var/www/steem-tools

ADD requirements.txt /var/www/steem-tools
RUN pip install -r requirements.txt

ADD . /var/www/steem-tools
