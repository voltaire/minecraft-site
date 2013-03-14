from flask import Flask
from flask.ext.mail import Mail, Message

mail = Mail()
app = Flask(__name__)
app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT='465',
        MAIL_USE_SSL=True,
        MAIL_USERNAME='nokbar@voltaire.sh',
        MAIL_PASSWORD='H3rpD3rpL0l')
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

