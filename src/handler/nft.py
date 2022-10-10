import json

from flask import request, make_response, render_template
from flask_restful import Resource
import requests
from src.models.nft_model import NftModel
from src.config import Config


class Nft(Resource):

    def get(self):
        # get argument from params
        args = request.args
        # nft address
        data = args['q']

        # set content type for html rendering
        headers = {
            "Content-Type": "text/html",
        }

        # search in db
        model = NftModel.search_by_name(data)

        # if model found in db, just return it to our template
        if model:
            payload = model.to_dict()
            return make_response(render_template('nft_info.html', payload=payload), headers)

        # else response with blockchain api
        mainnet = requests.get(
            "https://api.theblockchainapi.com/v1/solana/nft",
            params={
                # nft address searching param
                'mint_address': data,
                'network': 'mainnet-beta'
            },
            headers={
                'APISecretKey': Config.api_key,
                'APIKeyId': Config.api_id
            }
        )

        # all info about nft
        info = mainnet.json()

        # parse json
        try:
            payload = {
                "name": info["off_chain_data"]["name"],
                "address": info["mint"],
                "image": info["off_chain_data"]["image"],
                "description": info["off_chain_data"]["description"],
                "uri": info["data"]["uri"],
            }
        except KeyError:
            return make_response(render_template('error.html'), 404, headers)

        nft_model = NftModel(**payload)

        nft_model.save_to_db()
        return make_response(render_template('nft_info.html', payload=json.dumps(payload)), headers)
