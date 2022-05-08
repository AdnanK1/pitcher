from enum import unique
from .extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(length=30), nullable=False,unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)
