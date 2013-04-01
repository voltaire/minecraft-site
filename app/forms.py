from flask.ext.wtf import Form, TextField, BooleanField, Required, PasswordField, validators
import urllib

# 'http://minecraft.net/haspaid.jsp?user=' + field.data
"""
def mcHasPaid(field):
    message = '%s is not a Minecraft username or is not a paid Minecraft account.' % field.data

    def _mcHasPaid(form, field):
        mcun = field.data
        param = urllib.quote(mcun)
        f = urllib.urlopen("http://minecraft.net/haspaid.jsp?user=%s" % param)
        if f.read() == 'false':
            raise ValidationError(message)

    return _mcHasPaid
"""

class mcHasPaid(object):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        value = field.data
        valid = False
        if value:
            valid = self.check_mcUserHasPaid(value)

        if not valid:
            if self.message is None:
                self.message = field.gettext('Username does not have a paid Minecraft account.')
            raise validators.ValidationError(self.message)

    def check_mcUserHasPaid(self, value):
        param = urllib.quote(value)
        f = urllib.urlopen("http://minecraft.net/haspaid.jsp?user=%s" % param)
        if f.read() == 'false':
            raise False

class SignupForm(Form):
    mcuser = TextField('Minecraft Username', [
        validators.Length(max=16, message='Username too long'),
        validators.Regexp('\w', message='Illegal username'),
        mcHasPaid(),
        validators.Required(message='Enter your Minecraft Username')
        ])
    mcemail = TextField('Email Address', [
        validators.Length(min=6, max=35, message='Email needs to be between 6-35 characters'),
        validators.Required(message='Enter your email address'),
        validators.Email(message='Invalid email address')
        ])
    accept_tos = BooleanField('I accept the TOS', [
        validators.Required(message='Accept the TOS')
        ])

