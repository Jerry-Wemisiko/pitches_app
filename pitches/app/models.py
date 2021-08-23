from . import db,login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def login_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")   
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()
        
class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    info = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(user_id=id).all()
        return pitches

    @classmethod
    def get_user_pitches(cls,id):
        pitches = Pitch.query.filter_by(user_id= id).all()
        return pitches

    
class Comment(db.Model):
    __tablename__= 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    user_id =  db.Column(db.Integer, db.ForeignKey("users.id"))