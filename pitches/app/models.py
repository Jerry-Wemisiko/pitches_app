from operator import index
from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    about = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'user',lazy = 'dynamic')
    comments = db.relationship('Comment',backref = 'user', lazy = 'dynamic')

    

    def __repr__(self):
        return f'User {self.username}'

        
        
        
        