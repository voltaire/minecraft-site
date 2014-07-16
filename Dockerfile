FROM docku/uwsgi-python2
MAINTAINER Jon Chen <bsd@voltaire.sh>
ADD etc/nginx/mc-voltaire-sh.conf /etc/nginx/sites/
ADD etc/uwsgi/voltairemc.ini /etc/uwsgi/
