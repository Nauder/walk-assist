from exceptions import InvalidFieldException
from exceptions import UniqueViolationException
from extensions import db
from models import Usuario
from util.validator import validate_usuario, validate_put_usuario


def get_usuarios() -> list[Usuario]:
    return [usuario.as_dict() for usuario in Usuario.query.order_by(Usuario.registro).all()]


def get_usuario(registro: str) -> Usuario:
    usuario: Usuario = Usuario.query.filter(Usuario.registro == registro).first()

    return usuario.as_dict() if usuario is not None else {}


def post_usuario(usuario: dict[str, str]) -> Usuario:
    if validate_usuario(usuario):
        if bool(Usuario.query.filter(Usuario.registro == str(usuario.get('registro'))).first()):
            raise UniqueViolationException('registro', usuario.get('registro'))
        elif bool(Usuario.query.filter(Usuario.email == str(usuario.get('email'))).first()):
            raise UniqueViolationException('email', usuario.get('email'))
        else:
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
        raise InvalidFieldException("usuario")


def put_usuario(usuario: dict[str, str], registro: str) -> Usuario:
    if validate_put_usuario(usuario):
        existing_usuario: Usuario = Usuario.query.filter(Usuario.registro == registro).first()
        for key, value in usuario.items():
            setattr(existing_usuario, key, value)
        db.session.commit()
        return existing_usuario
    else:
        raise InvalidFieldException("usuario")


def delete_usuario(registro: str) -> None:
    existing_usuario: Usuario = Usuario.query.filter(Usuario.registro == registro).first()
    if existing_usuario is not None:
        db.session.delete(existing_usuario)
        db.session.commit()
    else:
        raise InvalidFieldException("registro")


def check_login(registro: str, password: str) -> bool:
    return bool(Usuario.query.filter(Usuario.registro == str(registro), Usuario.senha == str(password)).first())
