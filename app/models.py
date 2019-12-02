from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    password_hash=db.Column(db.String(255))
    # error defined
    @property
    def password(self):
        raise AttributeError("You Can't Read This Password")
    # password hashing and verifying in one decorator
    @password.setter
    def password(self, password):
        self.password_hash=generate_password_hash(password)
    # verify
    def verify(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):

        return f'User {self.username}'

class Quotes:

    def __init__(self, author, quote):
        self.author=author
        self.quote=quote
