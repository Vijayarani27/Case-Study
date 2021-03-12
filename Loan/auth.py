from flask import request, abort

import jwt
from functools import wraps

from microservice.model import User
from Loan import app


# validates the token
def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            abort(401, "Token is missing ")

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = User.query.filter_by(username=data['username']).first()
        except Exception:
            abort(401, "Token is Invalid ")

        return f(current_user, *args, **kwargs)
    return wrapper


# Gives the user object
@token_required
def get_user(current_user):
    print(current_user)
    return current_user
