from functools import wraps

from flask import request

from util.response_builder import build_response


def login_required(f):
    @wraps(f)
    def wrapped_view(**kwargs):
        auth = request.authorization
        if not (auth and check_auth(auth.username, auth.password)):
            return build_response(False, "unauthorized request", 401)

        return f(**kwargs)

    return wrapped_view


def admin_login_required(f):
    @wraps(f)
    def wrapped_view(**kwargs):
        auth = request.authorization
        if not (auth and check_admin_auth(auth.username, auth.password)):
            return build_response(False, "unauthorized request", 401)

        return f(**kwargs)

    return wrapped_view


def check_auth(username, password) -> bool:
    return True


def check_admin_auth(username, password) -> bool:
    print(f"{username}, {password}")
    return True
