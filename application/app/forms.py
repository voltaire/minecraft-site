from flask.ext.wtf import Form, TextField, BooleanField, Required, PasswordField, validators, HiddenField, RecaptchaField
from flask import request
import urllib

class mcHasPaid(object):
    def __init__(self, message=None):
        if not message:
            message = u'Username does not have a paid Minecraft account!'
        self.message = message

    def __call__(self, form, field):
      value = field.data
      param = urllib.quote(value)
      f = urllib.urlopen("http://minecraft.net/haspaid.jsp?user=%s" % param)
      if f.read() == 'false':
        raise validators.ValidationError(self.message)

class SignupForm(Form):
    applicant_ip = HiddenField([
        validators.IPAddress(ipv6=True),
        validators.Required(message='Contact the administrator.')
        ])
    mcuser = TextField('Minecraft Username:', [
        validators.Length(max=16, message='Username too long!'),
        validators.Regexp('\w', message='Illegal username!'),
        mcHasPaid(),
        validators.Required(message='Enter your Minecraft Username!')
        ])
    mcemail = TextField('Email Address:', [
        validators.Length(min=6, max=35, message='Email needs to be between 6-35 characters!'),
        validators.Required(message='Enter your email address!'),
        validators.Email(message='Invalid email address!')
        ])
    recaptcha = RecaptchaField()
    accept_tos = BooleanField('I accept the TOS.', [
        validators.Required(message='Please accept the TOS!')
        ])

