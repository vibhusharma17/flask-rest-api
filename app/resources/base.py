from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from app.helpers.exception import DataValidationError


class BaseResource(Resource):
    """
    All resource class should extend this class.
    """
    validator_class = None
    handler_class = None

    def validate_request(self):
        try:
            result = self.validator_class().load(request.json)
            return result
        except ValidationError as err:
            raise DataValidationError(err.messages)

    @staticmethod
    def response200(data):
        return data, 200

    @staticmethod
    def response201(data):
        return data, 201

    @staticmethod
    def response400(data):
        return data, 400
