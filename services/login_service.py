from exceptions.InvalidCredentialsException import InvalidCredentialsException
from security.token_manager import generate_token
from services.usuario_service import check_login
from util.validator import validate_login


def login(data: dict[str, str]) -> str:
    if validate_login(data) and check_login(data.get('registro'), data.get('senha')):
        return generate_token(data.get('registro'))
    else:
        raise InvalidCredentialsException()
