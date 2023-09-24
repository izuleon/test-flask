from functools import wraps

from flask import jsonify, request

from src.exception.generic_exception import UnauthorizedException

valid_token = ["3cdcnTiBsl"]


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        authorization_header = request.headers.get("Authorization")

        if authorization_header is None:
            raise UnauthorizedException(description="Missing Authorization Header")

        if authorization_header not in valid_token:
            raise UnauthorizedException(description="Invalid Token")
        return f(*args, **kwargs)

    return decorated_function
