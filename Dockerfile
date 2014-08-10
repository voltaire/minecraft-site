FROM dock0/service
MAINTAINER Jon Chen <bsd@voltaire.sh>

ADD . /srv/http/

RUN pacman -Syu --needed --noconfirm python2 python2-pip
RUN /usr/bin/pip2 install -r /srv/http/requirements.txt --upgrade

ONBUILD EXPOSE 8080
ONBUILD VOLUME ["/srv/db/", "/var/log/voltairemc"]
ONBUILD RUN /srv/http/manage.py db init
ONBUILD RUN /srv/http/manage.py db upgrade
ONBUILD RUN /srv/http/manage.py runserver -h 0.0.0.0 -p 8080 -R -D
