from exceptions import InvalidFieldException
from extensions import db
from models import Ponto
from util.validator import validate_ponto


def get_pontos() -> list[Ponto]:
    return [ponto.as_dict() for ponto in Ponto.query.all()]


def post_ponto(ponto: dict[str, str]) -> Ponto:
    if validate_ponto(ponto):
        new_ponto: Ponto = Ponto(ponto.get('nome'))
        db.session.add(new_ponto)
        db.session.commit()
        return new_ponto
    else:
        raise InvalidFieldException("")
