from datetime import datetime
from database import db

class Article(db.Model):
    __tablename__ = 'posts'

    title = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
