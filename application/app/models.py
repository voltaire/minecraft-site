from app import db

ROLE_USER = -1
ROLE_MEMBER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mcName = db.Column(db.String(16), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    #role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __init__(self, mcName, email):
      self.mcName = mcName
      self.email = email

    def __repr__(self):
        return '<User %r>' % (self.mcName)

class UserApplication(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self):
      self.body = body
      self.timestamp = timestamp
      self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % (self.body)
