from flask import Blueprint, request, Response
from flask_jwt_extended import jwt_required

from exceptions import InvalidFieldException
from services.ponto_service import get_pontos, post_ponto
from services.token_service import admin_required
from util.response_builder import build_response

ponto_mold = Blueprint("pontos", __name__)


@ponto_mold.get('/')
@jwt_required()
def get_pontos_route() -> Response:
    return build_response(
        True,
        "points obtained successfully",
        200,
        kwargs={'pontos': get_pontos()}
    )


@ponto_mold.post('/')
@jwt_required()
@admin_required
def post_ponto_route() -> Response:
    if request.mimetype == 'application/json':
        try:
            post_ponto(request.json)
            return build_response(True, "user created successfully", 201)
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
    else:
        return build_response(False, "unsupported media type", 415)
