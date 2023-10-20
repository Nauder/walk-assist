from exceptions.InvalidCredentialsException import InvalidCredentialsException
from exceptions.InvalidFieldException import InvalidFieldException
from extensions import db
from models import Usuario
from util.validator import validate_usuario


def get_usuarios() -> list[Usuario]:
    return [usuario.as_dict() for usuario in Usuario.query.all()]


def get_usuario(registro: str) -> Usuario:
    usuario = Usuario.query.filter(Usuario.registro == registro).first()

    return usuario.as_dict() if usuario is not None else {}


def post_usuario(usuario: dict[str, str]) -> Usuario:
    if validate_usuario(usuario):
        new_usuario: Usuario = Usuario(
            usuario.get('registro'),
            usuario.get('email'),
            usuario.get('senha'),
            usuario.get('nome'),
            usuario.get('tipo_usuario')
        )
        db.session.add(new_usuario)
        db.session.commit()
        return new_usuario
    else:
        raise InvalidFieldException("")


def put_usuario(usuario: dict[str, str], registro: str) -> Usuario:
    if validate_usuario(usuario):
        existing_usuario = Usuario.query.filter(Usuario.registro == registro).first()
        for key, value in usuario.items():
            setattr(existing_usuario, key, value)
        db.session.commit()
        return existing_usuario
    else:
        raise InvalidFieldException("")


def delete_usuario(usuario: dict[str, str], registro: str) -> None:
    if "senha" in usuario.keys():
        existing_usuario = Usuario.query.filter(Usuario.registro == registro).first()
        if existing_usuario is not None and existing_usuario.senha == usuario.get('senha'):
            db.session.delete(existing_usuario)
            db.session.commit()
        else:
            raise InvalidCredentialsException()
    else:
        raise InvalidFieldException("senha")


def check_login(registro: str, password: str) -> bool:
    return bool(Usuario.query.filter(Usuario.registro == str(registro), Usuario.senha == str(password)).first())
