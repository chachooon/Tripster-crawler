FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y software-properties-common curl \
    && add-apt-repository ppa:jonathonf/python-3.6 \
    && apt-get remove -y software-properties-common \
    && apt autoremove -y \
    && apt-get update \
    && apt-get install -y python3.6 \
    && curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \
    && python3.6 /tmp/get-pip.py \
    && apt-get remove -y curl \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD    ./manage.py            /app/
ADD    ./requirements.txt     /app/
RUN    pip install -r requirements.txt

ADD    ./tipstser/        /app/tipster/
RUN    ./manage.py collectstatic --noinput

CMD ["gunicorn", "--workers=3", "--bind", "0:8000", "djangosample.wsgi"]