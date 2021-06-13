FROM python:3.9.5

RUN pip install uwsgi

COPY . /home/www-data/local/www

RUN usermod -u 1000 www-data \
    && groupmod -g 1000 www-data

user www-data

WORKDIR /home/www-data/local/www

CMD uwsgi wsgi.ini