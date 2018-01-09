#!/bin/sh
pip install --user -r requirements.txt
python3.6 manage.py migrate

### model.py를 수정한경우 makemigrations 주석풀고 실행
python3.6 manage.py makemigrations
python3.6 manage.py migrate

### 장고 내장서버로 실행
python3.6 manage.py runserver 0:8000

### gunicorn으로 서버실행
# gunicorn --workers=3 --bind 0:8000 tipster.wsgi
