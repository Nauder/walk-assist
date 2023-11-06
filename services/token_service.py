from datetime import datetime, timezone
from functools import wraps

from flask_jwt_extended import JWTManager, get_jwt, decode_token

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


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if is_admin_token():
            return f(*args, **kwargs)
        return build_response(False, "user not authorized", 403)
    return decorated_function


def is_admin_token() -> bool:

    if "registro" in get_jwt().get('sub').keys():
        return get_usuario(get_jwt().get('sub').get("registro")).get("tipo_usuario") == 1

    return False


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None
