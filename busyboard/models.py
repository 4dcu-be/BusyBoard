from busyboard import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    busy = db.Column(db.Boolean)
    busy_with = db.Column(db.Text)
    can_be_disturbed = db.Column(db.Boolean)
    notes = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow)
