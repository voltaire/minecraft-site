from flask.ext.mail import Mail, Message

def testmail():
    msg = Message("Hello", sender=("flask", "flask@voltaire.sh"), recipients=["sjchen@sjchen.net"])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)

