#!/bin/bash

pip install django-oscar
pip uninstall pillow
apt-get -y install libjpeg-dev
pip install pillow
./manage.py syncdb --noinput
./manage.py migrate
./manage.py syncdb --all
./manage.py loaddata countries
