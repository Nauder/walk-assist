from datetime import datetime, timezone
from functools import wraps

from flask import jsonify
from flask_jwt_extended import JWTManager, get_jwt

from extensions import db
from models import TokenBlocklist
from services.usuario_service import get_usuario
from util.response_builder import build_response

jwt: JWTManager = JWTManager()


def modify_token() -> None:
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(jti=jti, created_at=now))
    db.session.commit()


def get_all_tokens() -> list[str]:
    return [token.jti for token in TokenBlocklist.query.all()]


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if is_admin_token():
            return f(*args, **kwargs)
        return build_response(False, "user not authorized", 403)
    return decorated_function


def is_self_or_admin() -> bool:
    if is_admin_token() or is_self_token():
        return True
    return False


def is_admin_token() -> bool:

    if "registro" in get_jwt().get('sub').keys():
        return get_usuario(str(get_jwt().get('sub').get("registro"))).get("tipo_usuario") == 1

    return False


def is_self_token() -> bool:
    return True


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload: dict):
    return jsonify({
        'success': False,
        'message': 'The token has expired'
    }), 401
