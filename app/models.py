from .extensions import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(length=30), nullable=False,unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)
    #user_comments = db.relationship('Comment', backref= 'user')
    #user_pitch = db.relationship('Pitch', backref= 'user')
    
    
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)


class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer(),primary_key = True)
    category = db.Column(db.String(),nullable=False)
    pitch = db.Column(db.String(), nullable=False,unique=True)
    #pitch_comment = db.relationship('Comment', backref= 'pitch')
    #user_id = db.Column(db.Integer(),db.ForeignKey('users.id'))
    
    
    

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(),nullable=False,unique=True )
    comment = db.Column(db.String(),nullable=False)
    #user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    #pitch_id = db.Column(db.Integer(), db.ForeignKey('pitch.id'))
    
