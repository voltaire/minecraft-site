FROM dock0/service
MAINTAINER Jon Chen <bsd@voltaire.sh>

VOLUME ["/etc/nginx/enabled-sites/"]

ADD etc/nginx/mc-voltaire-sh.conf /etc/nginx/enabled-sites/
ADD app /srv/http/

RUN pacman -Syu --needed --noconfirm python2 python2-pip
RUN /usr/bin/pip2 install -r /srv/http/app/requirements.txt --upgrade
