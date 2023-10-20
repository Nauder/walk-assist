from flask_jwt_extended import create_access_token

tokens: dict[str, str] = {}


def generate_token(registro: str) -> str:
    access_token = create_access_token(identity=registro)
    tokens[registro] = access_token
    return access_token
