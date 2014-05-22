#!/bin/bash
./manage.py dbcreate # Solucionar problema en syncdb --all
./manage.py syncdb --noinput
./manage.py migrate
./manage.py syncdb --all # Necesario para cargar permisos
mkdir -p public/media
mkdir -p public/static
./manage.py setpermissions
./manage.py collectstatic --noinput
./manage.py a2create
./manage.py loaddata countries
