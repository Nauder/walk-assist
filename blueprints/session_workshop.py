from flask import Blueprint, Response, request

from exceptions import InvalidFieldException
from services.session_service import get_sessions
from util.response_builder import build_response

session_mold = Blueprint("sessions", __name__)


@session_mold.get('')
def get_sessions_route() -> Response:
    if request.args['api_key'] == 'api123':
        try:
            return build_response(
                True,
                "sessions obtained successfully",
                200,
                kwargs={'sessions': get_sessions()}
            )
        except InvalidFieldException as ex:
            return build_response(False, str(ex), 422)
    else:
        return build_response(False, "user not authorized", 403)
