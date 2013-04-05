# voltaire-signups

Signups form on the website, using flask-email

# Configuration

make a file called ```application/config.py``` with the following contents:

  import os
  basedir = os.path.abspath(os.path.dirname(__file__))

  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

  MAIL_SERVER='your.mail.server'
  MAIL_PORT='mail.port'
  MAIL_USE_SSL=True
  MAIL_USERNAME='user@mail.server'
  MAIL_PASSWORD='mailpassword'

  CSRF_ENABLED = True
  SECRET_KEY = 'sekrit'

glhf
