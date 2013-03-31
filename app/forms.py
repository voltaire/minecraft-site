from flask.ext.wtf import Form, TextField, BooleanField, Required, PasswordField, validators

class SignupForm(Form):
    mcuser = TextField('Minecraft Username', [
        validators.Length(max=16, message='Username too long'),
        validators.Regexp([a-zA-Z0-9_], message='Invalid characters in username' 
        validators.Required(message='Enter your Minecraft Username')
        ])
    mcemail = TextField('Email Address', [
        validators.Length(min=6, max=35, message='
        Email needs to be between 6-35 characters'),
        validators.Required(message='Enter your email address'),
        validators.Email(message='Invalid email address')
        ])
    accept_tos = BooleanField('I accept the TOS', [
        validators.Required(message='Accept the TOS')
        ])

