from app import db
from app.models.manager import ModelManager


class Store(db.Model, ModelManager):
    __tablename__ = 'store'

    id = db.Column(db.Integer, primary_key=True)
    area_code = db.Column(db.String(256), index=False, unique=False, nullable=False)
    store_name = db.Column(db.String(256), index=False, unique=False, nullable=False)
    store_id = db.Column(db.String(256), index=False, unique=False, nullable=False)

    def __repr__(self):
        return '<STORE NAME {}>'.format(self.store_name)


class StoreDetails(db.Model, ModelManager):
    __tablename__ = 'store_details'

    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String(256), index=False, unique=False, nullable=False)
    image_url = db.Column(db.String(256), index=False, unique=False, nullable=False)
    perimeter = db.Column(db.Integer, index=False, unique=False, nullable=False)
    date = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __repr__(self):
        return '<STORE ID {} PERIMETER {}>'.format(self.store_id, self.perimeter)
