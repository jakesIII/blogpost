from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255), unique=True, index=True)
    password_hash=db.Column(db.String(255))
    avatar=db.Column(db.String())
    blog=db.relationship('Blog', backref='user', lazy=True)
    # error defined
    @property
    def password(self):
        raise AttributeError("You Can't Read This Password")
    # password hashing and verifying in one decorator
    @password.setter
    def password(self, password):
        self.password_hash=generate_password_hash(password)
    # verify
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):

        return f'User {self.username}'

class Blog(db.Model):
    __tablename__='blog'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String())
    content=db.Column(db.String())
    author=db.Column(db.String())
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    comments=db.relationship('Comments', backref='blog', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    def delete_blog(self):
        db.session.delete(self)
        db.session.commit

    @classmethod
    def get_blog(cls):
        blogs=Blog.query.all()
        return blogs
    @classmethod
    def get_user_blogs():
        user_blogs=Blog.query.filter_by(user_id=user_id).all()
        return user_blogs

class Comments(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String)
    user=db.Column(db.String)
    post_id=db.Column(db.Integer, db.ForeignKey('blog.id'))
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, post_id):
        comments=Comments.query.filter_by(post_id).all()
        return comments

class Quote:

    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
