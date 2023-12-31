from flask import Blueprint, request, Response
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

from exceptions import InvalidCredentialsException, InvalidFieldException, UniqueViolationException
from services.token_service import admin_required, is_self_or_admin
from services.usuario_service import get_usuarios, post_usuario, get_usuario, put_usuario, delete_usuario
from util.response_builder import build_response

usuario_mold: Blueprint = Blueprint("usuarios", __name__)


@usuario_mold.get('')
@jwt_required()
@admin_required
def get_usuarios_route() -> Response:
    return build_response(
        True,
        "users obtained successfully",
        200,
        kwargs={'usuarios': get_usuarios()}
    )


@usuario_mold.get('/<registro>')
@jwt_required()
def get_usuario_route(registro: str) -> Response:
    if is_self_or_admin():
        return build_response(
            True,
            "user obtained successfully",
            200,
            kwargs={'usuario': get_usuario(registro)}
        )
    else:
        return build_response(False, "user not authorized", 403)


@usuario_mold.post('')
@jwt_required()
@admin_required
@cross_origin(supports_credentials=True)
def post_usuario_route() -> Response:
    if request.mimetype == 'application/json':
        try:
            post_usuario(request.json)
            return build_response(True, "user created successfully", 200)
        except (InvalidFieldException, UniqueViolationException) as ex:
            return build_response(False, str(ex), 422)
    else:
        return build_response(False, "unsupported media type", 415)


@usuario_mold.put('/<registro>')
@jwt_required()
def put_usuario_route(registro: str) -> Response:
    if is_self_or_admin():
        try:
            put_usuario(request.json, registro)
            return build_response(True, "user edited successfully", 200)
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
    else:
        return build_response(False, "user not authorized", 403)


@usuario_mold.delete('/<registro>')
@jwt_required()
@cross_origin(supports_credentials=True)
def delete_usuario_route(registro: str) -> Response:
    if is_self_or_admin():
        try:
            delete_usuario(registro)
            return build_response(True, "user removed successfully", 200)
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
        except InvalidCredentialsException as ex:
            return build_response(False, str(ex), 401)
    else:
        return build_response(False, "user not authorized", 403)
