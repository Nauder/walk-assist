from flask import Blueprint, request, Response
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

from exceptions import InvalidFieldException, InvalidCredentialsException
from services.ponto_service import get_pontos, post_ponto, delete_ponto, get_ponto, put_ponto
from services.token_service import admin_required
from util.response_builder import build_response

ponto_mold = Blueprint("pontos", __name__)


@ponto_mold.get('')
@jwt_required()
def get_pontos_route() -> Response:
    return build_response(
        True,
        "points obtained successfully",
        200,
        kwargs={'pontos': get_pontos()}
    )


@ponto_mold.get('/<ponto_id>')
@jwt_required()
def get_ponto_route(ponto_id: int) -> Response:
    return build_response(
        True,
        "point obtained successfully",
        200,
        kwargs={'ponto': get_ponto(ponto_id)}
    )


@ponto_mold.put('/<ponto_id>')
@jwt_required()
@admin_required
def put_ponto_route(ponto_id: int) -> Response:
    try:
        put_ponto(request.json, ponto_id)
        return build_response(True, "point edited successfully", 200)
    except InvalidFieldException as ex:
        return build_response(False, str(ex), 422)


@ponto_mold.post('')
@jwt_required()
@admin_required
def post_ponto_route() -> Response:
    if request.mimetype == 'application/json':
        try:
            post_ponto(request.json)
            return build_response(True, "point created successfully", 200)
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
    else:
        return build_response(False, "unsupported media type", 415)


@ponto_mold.delete('/<ponto_id>')
@jwt_required()
@admin_required
@cross_origin(supports_credentials=True)
def delete_ponto_route(ponto_id: int) -> Response:
    try:
        delete_ponto(ponto_id)
        return build_response(True, "point removed successfully", 200)
    except InvalidFieldException as ex:
        return build_response(False, str(ex), 422)
    except InvalidCredentialsException as ex:
        return build_response(False, str(ex), 401)
