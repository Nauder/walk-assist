from typing import Any

from flask import make_response, jsonify, Response


def build_response(success:  bool, message: str | list, status_code: int, **kwargs:  dict[str, Any]) -> Response:

    return make_response(jsonify((kwargs.get('kwargs') if kwargs.get('kwargs') is not None else {}) | {
        'success': success,
        'message': message
    }), status_code)
