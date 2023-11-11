from flask import Blueprint, request, Response, current_app
from flask_jwt_extended import jwt_required

from exceptions.InvalidCredentialsException import InvalidCredentialsException
from exceptions.InvalidFieldException import InvalidFieldException
from services.login_service import login, logout
from util.response_builder import build_response

login_mold = Blueprint("login", __name__)


@login_mold.post('/login')
def login_route():
    if request.mimetype == 'application/json':
        try:
            response: Response = build_response(True, "login successful", 200, kwargs={
                'token': login(request.json),
                'registro': request.json.get('registro')
            })
            current_app.logger.info(f'OUT >> {response.json}')
            return response
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
        except InvalidCredentialsException as ex:
            return build_response(False, str(ex), 401)
    else:
        return build_response(False, "unsupported media type", 415)


@login_mold.post('/logout')
@jwt_required()
def logout_route():
    logout()
    response = build_response(True, "logout successful", 201)
    current_app.logger.info(f'OUT >> {response.json}')
    return response
