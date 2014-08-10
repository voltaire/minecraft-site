FROM dock0/service
MAINTAINER Jon Chen <bsd@voltaire.sh>

ADD . /srv/http/

RUN pacman -Syu --needed --noconfirm python2 python2-pip
RUN /usr/bin/pip2 install -r /srv/http/requirements.txt --upgrade
