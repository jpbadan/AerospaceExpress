from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    about = db.Column(db.String(256))
    kharma = db.Column(db.Integer, default=0)
    # posts =
    # likes =
    # favs =
    # hiden =

    def __repr__(self):
        return f"User('{self.userName}', '{self.email}', '{self.createdAt}, '{self.kharma})"


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(256), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    ranking = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)

    postedBy = db.relationship("User", backref="posts")

    def __repr__(self):
        return f"Post('{self.id}, \
                      '{self.title}', \
                      '{self.url}', \
                      '{self.postedBy}, \
                      '{self.createdAt}, \
                      '{self.ranking}', \
                      '{self.likes})"
