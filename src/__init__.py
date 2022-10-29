from flask import Flask
from flask_restful import Api
from src.handler.search import Search
from src.handler.nft import Nft
from src.handler.auth import Register, Login
from src.handler.home import Home
from src.config import Config
from src.db import db
from flask_migrate import Migrate

migrate = Migrate()
api = Api()

username = Config.user_db
password = Config.password_db
dbname = Config.dbname


def create_app(config_filename=None):
    app = Flask(__name__, static_url_path='/static')
    api = initialize_api(app)
    migrate.init_app(app, db)
    register_resources(api)
    config_db(app, db)
    return app


def initialize_api(app):
    api = Api(app)
    return api


def register_resources(api):
    api.add_resource(Register, "/api/user/signup")
    api.add_resource(Search, "/api/search")
    api.add_resource(Nft, "/api/nft")
    api.add_resource(Home, "/")
    api.add_resource(Login, "/api/user/signin")


def config_db(app, db):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
