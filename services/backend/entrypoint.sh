#!/bin/sh

python src/manage.py migrate
python src/manage.py collectstatic --noinput

exec "$@"
