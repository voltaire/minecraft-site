#!/usr/bin/env python
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
import app

migrate = Migrate(app.app, app.db)

manager = Manager(app.app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
