from flask import Blueprint, Response

from exceptions import InvalidFieldException
from services.session_service import get_sessions
from util.response_builder import build_response

session_mold = Blueprint("sessions", __name__)


@session_mold.get('')
def get_sessions_route() -> Response:
    try:
        return build_response(
            True,
            "sessions obtained successfully",
            200,
            kwargs={'sessions': get_sessions()}
        )
    except InvalidFieldException as ex:
        return build_response(False, str(ex), 422)
