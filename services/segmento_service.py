from exceptions.InvalidFieldException import InvalidFieldException
from extensions import db
from models import Segmento
from util.validator import validate_segmento


def get_segmentos() -> list[Segmento]:
    return [segmento.as_dict() for segmento in Segmento.query.all()]


def post_segmento(segmento: dict[str, str]) -> Segmento:

    if validate_segmento(segmento):
        new_segmento: Segmento = Segmento(
            segmento.get('distancia'),
            segmento.get('ponto_inicial'),
            segmento.get('ponto_final'),
            segmento.get('status'),
            segmento.get('direcao')
        )
        db.session.add(new_segmento)
        db.session.commit()
        return new_segmento
    else:
        raise InvalidFieldException("")


def put_segmento(segmento: dict[str, str], id_segmento: int) -> Segmento:
    if validate_segmento(segmento):
        existing_segmento = Segmento.query.filter(Segmento.id_segmento == id_segmento).first()
        for key, value in segmento.items():
            setattr(existing_segmento, key, value)
        db.session.commit()
        return existing_segmento
    else:
        raise InvalidFieldException("")


def delete_segmento(segmento: dict[str, str], id_segmento: int) -> None:
    if "senha" in segmento.keys():
        existing_segmento = Segmento.query.filter(Segmento.id_segmento == id_segmento).first()
        if existing_segmento is not None:
            db.session.delete(existing_segmento)
            db.session.commit()
        else:
            raise InvalidFieldException("id_segmento")
    else:
        raise InvalidFieldException("senha")
