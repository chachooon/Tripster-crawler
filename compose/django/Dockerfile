FROM ubuntu:16.04

ENV PYTHONUNBUFFERED=0
ENV PATH=${PYTHONUSERBASE}lib/python3.6/site-packages/bin:${PATH}

RUN apt-get update \
    && apt-get install -y software-properties-common curl \
    && add-apt-repository ppa:jonathonf/python-3.6 \
    && apt-get remove -y software-properties-common \
    && apt autoremove -y \
    && apt-get update \
    && apt-get install -y python3.6 \
    && curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \
    && python3.6 /tmp/get-pip.py \
    && apt-get -y install libpq-dev python-dev \
    && apt-get remove -y curl \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD    ./manage.py                    /app/

ADD    compose/django/start-dev.sh       /start-dev.sh
RUN    chmod +x /*.sh
