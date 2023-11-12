from flask_jwt_extended import create_access_token

from exceptions import InvalidCredentialsException
from services.token_service import modify_token
from services.usuario_service import check_login
from util.validator import validate_login


def login(data: dict[str, str]) -> str:
    if validate_login(data) and check_login(data.get('registro'), data.get('senha')):
        return create_access_token(identity={
            "registro": data.get('registro'),
            "senha": data.get('senha')
        })
    else:
        raise InvalidCredentialsException()


def logout() -> None:
    modify_token()
