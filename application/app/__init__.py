from flask import Flask
from flask.ext.mail import Mail, Message
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)
db = SQLAlchemy(app)

from app import views, models

