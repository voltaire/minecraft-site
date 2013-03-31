from flask import render_template
from app import app

@app.route("/")
def index():
    msg = Message("Hello", sender=("flask", "flask@voltaire.sh"), recipients=["sjchen@sjchen.net"])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)
    return msg.html

@app.route("/submit_application", methods=['POST'])
def submit_application:

