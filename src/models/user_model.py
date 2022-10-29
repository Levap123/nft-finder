import os
import jwt
from flask import request
from src.db import db
from passlib.apps import custom_app_context as pwd_context


class UserModel(db.Model):
    __tablename__ = 'users'

    # user entity fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(255), unique=True)

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    def hash_password(self):
        self.password_hash = pwd_context.encrypt(self.password_hash)

    # safe user to db
    def save_to_db(self):
        self.hash_password()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_pass(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if not pwd_context.verify(password, user.password_hash):
            return None
        return user

    @classmethod
    def search_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        return user

    @classmethod
    def search_by_id(cls, id):
        user = cls.query.filter_by(id=id).first()
        return user


def parse_token():
    token = request.cookies.get('x-access-token')
    if token is None:
        return None
    try:
        data = jwt.decode(token, os.getenv("SIGN_KEY"), algorithms='HS256')
        print(data)
        current_user = UserModel.search_by_username(data['username'])
    except:
        return None
    return current_user


def generate_token(username: str):
    return jwt.encode({'username': username}, os.getenv("SIGN_KEY"), algorithm='HS256')
