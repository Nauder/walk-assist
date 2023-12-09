from flask_jwt_extended import create_access_token

from exceptions import InvalidCredentialsException
from services.session_service import post_session, delete_session
from services.token_service import modify_token
from services.usuario_service import check_login
from util.validator import validate_login


def login(data: dict[str, str]) -> str:
    if validate_login(data) and check_login(data.get('registro'), data.get('senha')):
        post_session(data.get('registro'))
        return create_access_token(identity={
            "registro": data.get('registro'),
            "senha": data.get('senha')
        })
    else:
        raise InvalidCredentialsException()


def logout() -> None:
    delete_session()
    modify_token()
