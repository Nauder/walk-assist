from flask_jwt_extended import get_jwt

from exceptions import InvalidFieldException
from extensions import db
from models import Session, Usuario


def get_sessions() -> list[Session]:
    return [session.as_dict() for session in Session.query.order_by(Session.registro).all()]


def post_session(registro: str) -> None:
    usuario: Usuario = Usuario.query.filter(Usuario.registro == registro).first()
    db.session.add(Session(
        usuario.registro,
        usuario.email,
        usuario.nome,
        'administrador' if usuario.tipo_usuario == 1 else 'comum'
    ))
    db.session.commit()


def delete_session() -> None:
    existing_session: Session = Session.query.filter(Session.registro == get_jwt()['sub']['registro']).first()
    if existing_session is not None:
        db.session.delete(existing_session)
        db.session.commit()
    else:
        raise InvalidFieldException("registro")
