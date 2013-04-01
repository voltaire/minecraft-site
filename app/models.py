from app import db

ROLE_USER = -1
ROLE_MEMBER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mcName = db.Column(db.String(16), index = True, Unique = True)
    email = db.Column(db.String(120), index = True, Unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.mcName)

