#!/bin/sh

exec usr/bin/uwsgi --master --processes 4 --threads 2 --ini /etc/uwsgi/voltairemc.ini 2>&1
