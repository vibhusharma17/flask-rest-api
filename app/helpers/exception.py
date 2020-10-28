from werkzeug.exceptions import BadRequest


class DataValidationError(BadRequest):
    pass


class FileNotFound(Exception):
    pass


class InvalidDataType(Exception):
    pass
