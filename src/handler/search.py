from flask import render_template, make_response
from flask_restful import Resource
from src.models.user_model import parse_token


class Search(Resource):

    def get(self):
        user = parse_token()
        headers = {'Content-Type': 'text/html'}
        if user is None:
            return "not authorized"
        payload = {
            'user': user.username,
        }
        return make_response(render_template('nft_searchbar.html', payload=payload), 200,
                             headers, )
