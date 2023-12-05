from exceptions import InvalidFieldException
from extensions import db
from models import Ponto
from util.validator import validate_ponto


def get_pontos() -> list[Ponto]:
    return [ponto.as_dict() for ponto in Ponto.query.all()]


def get_ponto(ponto_id: int) -> dict:
    ponto: Ponto = Ponto.query.filter(Ponto.ponto_id == ponto_id).first()

    return ponto.as_dict() if ponto is not None else {}


def post_ponto(ponto: dict[str, str]) -> Ponto:
    if validate_ponto(ponto):
        new_ponto: Ponto = Ponto(ponto.get('nome'))
        db.session.add(new_ponto)
        db.session.commit()
        return new_ponto
    else:
        raise InvalidFieldException("ponto")


def put_ponto(ponto: dict[str, str], ponto_id: int) -> Ponto:
    if "nome" in ponto.keys():
        existing_ponto: Ponto = Ponto.query.filter(Ponto.ponto_id == ponto_id).first()
        for key, value in ponto.items():
            setattr(existing_ponto, key, value)
        db.session.commit()
        return existing_ponto
    else:
        raise InvalidFieldException("nome")


def delete_ponto(ponto_id: int) -> None:
    existing_ponto: Ponto = Ponto.query.filter(Ponto.ponto_id == ponto_id).first()
    if existing_ponto is not None:
        db.session.delete(existing_ponto)
        db.session.commit()
    else:
        raise InvalidFieldException("ponto_id")
