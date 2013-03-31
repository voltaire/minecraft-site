from flask import Flask

mail = Mail()
app = Flask(__name__)
app.config.from_object('config')
mail.init_app(app)

from app import views
