from sqlalchemy_serializer import SerializerMixin
from src.db import db


class NftModel(db.Model, SerializerMixin):
    __tablename__ = 'nfts'

    serialize_only = ('id', 'name', 'description', 'image', 'uri', 'address')

    # nft entity fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))
    image = db.Column(db.String(255))
    uri = db.Column(db.String(255))
    address = db.Column(db.String(255))

    # safe nft to db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def search_by_name(cls, address):
        return cls.query.filter_by(address=address).first()
