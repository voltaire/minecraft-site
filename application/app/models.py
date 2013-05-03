from sqlalchemy.dialects import postgresql
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mcuser = db.Column(db.String(16), index = True, unique = True)
    mcemail = db.Column(db.String(120), index = True, unique = True)
    applicant_age = db.Column(db.SmallInteger(), default = 15)
    applicant_skills = db.Column(db.String(), index = True, unique = False)
    applicant_ip = db.Column(db.String(120), index = True, unique = True)
    fishbanned = db.Column(db.Boolean(), index = True, unique = False)

    def __init__(self, mcuser=None, mcemail=None, applicant_age=None, applicant_skills=None, applicant_ip=None, fishbanned=None):
      self.mcuser = mcuser
      self.mcemail = mcemail
      self.applicant_age = applicant_age
      self.applicant_skills = applicant_skills
      self.applicant_ip = applicant_ip
      self.fishbanned = fishbanned

    def __repr__(self):
        return '<User %r>' % (self.mcuser)

class MinecraftServers(db.Model):


    id = db.Column(db.Integer, primary_key = True)
    server_name = db.Column(db.String(140))
    server_address = db.Column(postgresql.INET)
    server_port = db.Column(db.SmallInteger())

    def __init__(self, server_name=None, server_address=None, server_port=None):
        self.server_name = server_name
        self.server_address = server_address
        self.server_port = server_port

    def __repr__(self):
        return '<Server %r>' % (self.server_name)

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
