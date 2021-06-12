FROM python:3.9.5

RUN pip install uwsgi

COPY . /var/www

WORKDIR /var/www

CMD uwsgi --http :80 --master --processes 2 --threads 2 --wsgi-file /var/www/index.py