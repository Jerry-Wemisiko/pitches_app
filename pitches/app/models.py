from . import db,login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def login_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(3255),unique= True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments = db.relationship('Comment',backref = 'users',lazy= 'dynamic')
    pass_secure = db.Column(db.String(255))
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
        
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __table__name__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    info = db.Column(db.String)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'users',lazy= 'dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f'Pitch {self.info}'

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    user_id =  db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_comments(cls,pitch_id):
        comment = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comment
    
    def __repr__(self):
        return f'Comment {self.comment}'


    


    


    


    

    

    

