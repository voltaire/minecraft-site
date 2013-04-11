from flask import Flask
from flask.ext.mail import Mail, Message
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)
db = SQLAlchemy(app)
babel = Babel(app)

if not app.debug:
    import logging
    from logging import Formatter, getLogger
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler('logs/errors.log')
    file_handler.setLevel(logging.WARNING)

    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'))

    mail_handler.setFormatter(Formatter('''
        Message type:       %(levelname)s
        Location:           %(pathname)s:%(lineno)d
        Module:             %(module)s
        Function:           %(funcName)s
        Time:               %(asctime)s

        Message:

        %(message)s
        '''))

    app.log.addHandler(file_handler)
    app.log.addHandler(mail_handler)

    loggers = [app.logger, getLogger('sqlalchemy')]
    for logger in loggers:
        logger.addHandler(mail_handler)
        logger.addHandler(file_handler)

from app import views, models

