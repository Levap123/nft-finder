from flask import make_response, render_template, request, redirect
from flask_restful import reqparse, Resource
from src.models.user_model import UserModel
from src.models.user_model import generate_token


class Register(Resource):
    def post(self):
        form = request.form
        credentials = {
            "username": form['username'],
            "password_hash": form['password'],
        }
        user = UserModel(**credentials)
        try:
            user.save_to_db()
        except:
            return 'user with this username already exist'
        resp = make_response(redirect("/api/user/signin", 301))
        resp.set_cookie('x-access-token', '', max_age=60 * 60 * 24 * 365 * 2)
        return resp

    def get(self):
        headers = {
            "Content-Type": "text/html",
        }
        return make_response(render_template('register.html'), headers)


class Login(Resource):
    def post(self):
        name = request.form['username']
        user = UserModel.check_pass(name, request.form['password'])
        if user is None:
            return "bad credentials"
        token = generate_token(name)
        res = make_response(redirect("/api/search", 301))
        res.set_cookie('x-access-token', token, max_age=60 * 60 * 24 * 365 * 2)
        return res

    def get(self):
        headers = {
            "Content-Type": "text/html",
        }
        return make_response(render_template('login.html'), headers)
