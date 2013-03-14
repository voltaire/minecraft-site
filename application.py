from flask import Flask
from flask.ext.mail import Mail, Message

mail = Mail()
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('application.cfg', silent=True)
mail.init_app(app)

@app.route("/")
def index():
    msg = Message("Hello", sender=("flask", "flask@voltaire.sh"), recipients=["sjchen@sjchen.net"])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)
    return msg.html

if __name__ == '__main__':
    app.run()

