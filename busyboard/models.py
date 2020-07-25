from busyboard import db, images
from datetime import datetime
import arrow


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
        if self.path is None:
            return
        return images.url(self.path)

    @property
    def filepath(self):
        if self.path is None:
            return
        return images.path(self.path)

    @property
    def last_changed(self):
        age_arrow = arrow.get(self.last_change)
        return age_arrow.humanize()

    @staticmethod
    def on_change(mapper, connection, target):
        target.last_change = datetime.utcnow()


db.event.listen(User, 'before_update', User.on_change)
