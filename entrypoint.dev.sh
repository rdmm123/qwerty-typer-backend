#!/bin/bash
# Make migrations and migrate
# python manage.py makemigrations --no-input
# mkmg_status=$?
# if [ $mkmg_status -ne 0 ]
# then
#   exit $mkmg_status
# fi
# python manage.py migrate --no-input
# Collect static files
pip install debugpy -t /tmp
python /tmp/debugpy --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000