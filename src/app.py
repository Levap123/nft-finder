from flask import Flask
from flask_restful import Api
from src.db import db
from src.handler.home import Home
from src.handler.nft import Nft

username = "postgres"
password = "postgres"
dbname = "ass3"

if __name__ == '__main__':
    app = Flask(__name__, static_url_path='/static')
    api = Api(app)
    api.add_resource(Home, "/")
    api.add_resource(Nft, "/api/v1/nft")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=False, port="17792")
