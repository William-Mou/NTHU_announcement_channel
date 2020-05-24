FROM alpine:latest
# This hack is widely applied to avoid python printing issues in docker containers.
ENV PYTHONUNBUFFERED 1
# Install python3 & pip3
RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
RUN apk add --update --no-cache g++ gcc libxslt-dev python3-dev

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt

# 新增 .env
RUN cp .env-example .env

# 建立資料表
RUN python3 manage.py migrate

ENTRYPOINT ['python3', 'manage.py', 'runserver']
