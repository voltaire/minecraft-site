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

### LICENSE
Copyright (c) 2013, [fly](https://github.com/fly)
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


