from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, BooleanField, HiddenField, IntegerField, \
    TextAreaField
from wtforms.validators import ValidationError, IPAddress, Required, Length, \
    Email, NumberRange, Regexp
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
            raise ValidationError(self.message)


class SignupForm(Form):

    applicant_ip = HiddenField([
        IPAddress(ipv6=True),
        Required(message='Contact the administrator.')
        ])

    mcuser = TextField('Minecraft Username:', [
        Length(max=16, message='Username too long!'),
        Regexp('\w', message='Illegal username!'),
        mcHasPaid(),
        Required(message='Enter your Minecraft Username!')
        ])

    mcemail = TextField('Email Address:', [
        Length(min=6, max=35,
               message='Email needs to be between 6-35 characters!'),
        Required(message='Enter your email address!'),
        Email(message='Invalid email address!')
        ])

    applicant_age = IntegerField('Age:', [
        NumberRange(min=15, message='Sorry, come back later!'),
        Required(message='Enter your age!')
        ])

    applicant_skills = TextAreaField('Particular Skills:', [
        Length(min=3, max=500,
               message='Write more or keep it under 500 characters.'),
        Required(message='Please write something here.')
        ])

    recaptcha = RecaptchaField()

    accept_tos = BooleanField('I accept the TOS.', [
        Required(message='Please accept the TOS!')
        ])
