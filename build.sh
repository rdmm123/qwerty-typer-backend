#!/usr/bin/env bash
# Make migrations and migrate
pip install -r requirements.txt

python manage.py makemigrations --no-input
mkmg_status=$?
if [ $mkmg_status -ne 0 ]
then
  exit $mkmg_status
fi
python manage.py migrate --no-input
