from flask import Blueprint, request, Response

from exceptions.InvalidFieldException import InvalidFieldException
from security.login_manager import admin_login_required
from services.ponto_service import get_pontos, post_ponto
from util.response_builder import build_response

ponto_mold = Blueprint("pontos", __name__)


@ponto_mold.get('/')
@admin_login_required
def get_pontos_route() -> Response:
    return build_response(
        True,
        "points obtained successfully",
        200,
        kwargs={'pontos': get_pontos()}
    )


@ponto_mold.post('/')
@admin_login_required
def post_ponto_route() -> Response:
    if request.mimetype == 'application/json':
        try:
            post_ponto(request.json)
            return build_response(True, "user created successfully", 201)
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
    else:
        return build_response(False, "unsupported media type", 415)
