from flask import Flask
from flask.ext.mail import Mail, Message

mail = Mail()
app = Flask(__name__)
app.config.from_object('config')
mail.init_app(app)

from app import views
