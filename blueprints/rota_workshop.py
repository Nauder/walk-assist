from flask import Blueprint, request, Response
from flask_jwt_extended import jwt_required

from exceptions import InvalidFieldException
from services.rota_service import get_rota
from util.response_builder import build_response

rota_mold = Blueprint("rotas", __name__)


@rota_mold.post('')
@jwt_required()
def post_rota_route() -> Response:
    if request.mimetype == 'application/json':
        try:
            return build_response(
                True,
                "rota obtained successfully",
                200,
                kwargs={'rota': get_rota(request.json)}
            )
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
        except KeyError:
            return build_response(False, 'a route could not be made between the given points', 422)
    else:
        return build_response(False, "unsupported media type", 415)
