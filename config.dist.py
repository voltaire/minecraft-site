import os
basedir = os.path.abspath(os.path.dirname(__file__))

MCSERVERS = [
    {'name': 'vanilla', 'hostname': 'mc.voltaire.sh', 'port': '25565'},
    {'name': 'creative', 'hostname': 'create.voltaire.sh', 'port': '25567'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = '465'
MAIL_USE_SSL = True
MAIL_USERNAME = 'no-reply@voltaire.sh'
MAIL_PASSWORD = 'password'

ADMINS = ['bsd@voltaire.sh']

RECAPTCHA_USE_SSL = True
RECAPTCHA_PRIVATE_KEY = 'privkey'
RECAPTCHA_PUBLIC_KEY = 'pubkey'

CSRF_ENABLED = True
SECRET_KEY = 'supersekrit'
