from flask import Blueprint, request, Response

from exceptions.InvalidCredentialsException import InvalidCredentialsException
from exceptions.InvalidFieldException import InvalidFieldException
from security.login_manager import admin_login_required
from services.login_service import login
from services.usuario_service import get_usuarios, post_usuario, get_usuario, put_usuario, delete_usuario
from util.response_builder import build_response

login_mold = Blueprint("login", __name__)


@login_mold.post('/login')
def login_route():
    if request.mimetype == 'application/json':
        try:
            return build_response(True, "user created successfully", 201, kwargs={
                'token': login(request.json)
            })
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
        except InvalidCredentialsException as ex:
            return build_response(False, str(ex), 401)
    else:
        return build_response(False, "unsupported media type", 415)


@login_mold.post('/logout')
def logout_route():
    if request.mimetype == 'application/json':
        try:
            post_usuario(request.json)
            return build_response(True, "user created successfully", 201)
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
    else:
        return build_response(False, "unsupported media type", 415)
