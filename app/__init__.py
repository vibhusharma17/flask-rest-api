import redis
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.celery import make_celery

db = SQLAlchemy()


def create_app(test_connection=False):
    app = Flask(__name__)

    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379',
        CELERY_RESULT_BACKEND='redis://localhost:6379',
        SQLALCHEMY_DATABASE_URI='sqlite:///abcde.sqlite',
    )
    if test_connection is True:
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.sqlite',
        )
    db.init_app(app)
    return app


# app = Flask(__name__)
# api = Api(app)
#
# app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379',
#     CELERY_RESULT_BACKEND='redis://localhost:6379',
#     SQLALCHEMY_DATABASE_URI='sqlite:///abcde.sqlite',
# )
#
# db = SQLAlchemy()
# redis_db = redis.StrictRedis('localhost')
# db.init_app(app)


def make_rest_api(app):
    api = Api(app)
    return api


app = create_app()
api = make_rest_api(app)
celery = make_celery(app)
redis_db = redis.StrictRedis('localhost')

from app.router import *
