from flask import Blueprint, request, Response
from flask_jwt_extended import jwt_required

from exceptions import InvalidCredentialsException
from exceptions import InvalidFieldException
from services.segmento_service import put_segmento, delete_segmento, post_segmento, get_segmentos, get_segmento
from util.response_builder import build_response

segmento_mold = Blueprint("segmentos", __name__)


@segmento_mold.get('')
@jwt_required()
def get_segmentos_route() -> Response:
    return build_response(
        True,
        "segments obtained successfully",
        200,
        kwargs={'segmentos': get_segmentos()}
    )


@segmento_mold.get('/<segmento_id>')
@jwt_required()
def get_segmento_route(segmento_id: int) -> Response:
    return build_response(
        True,
        "segment obtained successfully",
        200,
        kwargs={'segmento': get_segmento(segmento_id)}
    )


@segmento_mold.post('')
@jwt_required()
def post_segmento_route() -> Response:
    if request.mimetype == 'application/json':
        try:
            post_segmento(request.json)
            return build_response(True, "segment created successfully", 200)
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
    else:
        return build_response(False, "unsupported media type", 415)


@segmento_mold.put('/<segmento_id>')
@jwt_required()
def put_segmento_route(segmento_id: int) -> Response:
    try:
        put_segmento(request.json, segmento_id)
        return build_response(True, "segment edited successfully", 200)
    except InvalidFieldException as ex:
        return build_response(False, str(ex), 422)


@segmento_mold.delete('/<segmento_id>')
@jwt_required()
def delete_segmento_route(segmento_id: int) -> Response:
    try:
        delete_segmento(segmento_id)
        return build_response(True, "segment removed successfully", 200)
    except InvalidFieldException as ex:
        return build_response(False, str(ex), 422)
    except InvalidCredentialsException as ex:
        return build_response(False, str(ex), 401)
