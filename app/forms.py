from flask.ext.wtf import Form, TextField, BooleanField, Required, PasswordField, validators

class SignupForm(Form):
    mcuser = TextField('Minecraft Username', [
        validators.Length(max=16),
        validators.Required()
        ])
    mcemail = TextField('Email Address', [
        validators.Length(min=6, max=35),
        validators.Required()
        ])
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

