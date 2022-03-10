#!/bin/sh

set -e
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
case "$1" in
start)
  echo "Running migrate to DB..."
  exec python manage.py migrate
  exec python manage.py collectstatic --noinput
  ;;
*)
  exec $@
  ;;
esac