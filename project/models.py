from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(64), unique = True)
  password = db.Column(db.String(10))
  name = db.Column(db.String(64))