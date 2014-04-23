# mc.voltaire.sh

#### Errata:
* Create a config file in ```application/config.py``` with the following contents:

```python
import os

CSRF_ENABLED = True
SECRET_KEY = 'SEKRIT SEKRIT'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER='your.mail.server'
MAIL_PORT='mail.port'
MAIL_USE_SSL=True
MAIL_USERNAME='user@mail.server'
MAIL_PASSWORD='mailpassword'

RECAPTCHA_USE_SSL=True
RECAPTCHA_PRIVATE_KEY='privkey here'
RECAPTCHA_PUBLIC_KEY='privkey here'

MCSERVERS = [
        { 'name': 'vanilla',  'hostname': 'ip.addr.here',     'port': '25565' },
        { 'name': 'ftb',      'hostname': 'ip.addr.here',     'port': '25565' },
        { 'name': 'creative', 'hostname': 'ip.addr.here',     'port': '25565' }]
```

### Thanks to:
* [Dinnerbone](https://github.com/Dinnerbone)
* [Jinja2](http://jinja.pocoo.org/)
* [Flask](http://flask.pocoo.org/)
* [Python](http://www.python.org/)
* [goldblattster for fishbans-python](https://github.com/goldblattster/fishbans-python)
