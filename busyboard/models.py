from busyboard import db, images
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    busy = db.Column(db.Boolean)
    busy_with = db.Column(db.Text)
    can_be_disturbed = db.Column(db.Boolean)
    notes = db.Column(db.Text)
    path = db.Column(db.Unicode(128))
    last_change = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def url(self):
        return images.url(self.filename)

    @property
    def filepath(self):
        if self.filename is None:
            return
        return images.path(self.filename)

