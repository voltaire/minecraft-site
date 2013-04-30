from flask.ext.mail import Mail, Message
from flask import render_template
from app import app, mail
from config import ADMINS

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def testmail():
    msg = Message("Hello", sender=("flask", "flask@voltaire.sh"), recipients=["sjchen@sjchen.net"])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)

def SignupAlert(mcuser, mcemail, applicant_ip, applicant_age, applicant_skills, tb):
    msg = Message("Signup Alert",
                  sender=("flask", "flask@voltaire.sh"),
                  recipients=ADMINS)
    msg.body = render_template("signupalert_email.txt",
                               mcuser=mcuser,
                               mcemail=mcemail,
                               applicant_ip=applicant_ip,
                               applicant_age=applicant_age,
                               applicant_skills=applicant_skills,
                               tb=tb)
    mail.send(msg)

