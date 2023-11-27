from exceptions import InvalidFieldException
from extensions import db
from models import Segmento
from services.ponto_service import get_ponto
from util.validator import validate_segmento


def get_segmentos() -> list[Segmento]:
    segmentos: list = [segmento.as_dict() for segmento in Segmento.query.all()]

    for segmento in segmentos:
        segmento['ponto_inicial'] = get_ponto(segmento['ponto_inicial']).get('nome')
        segmento['ponto_final'] = get_ponto(segmento['ponto_final']).get('nome')

    return segmentos


def get_segmento(segmento_id: int) -> dict:
    segmento: Segmento = Segmento.query.filter(Segmento.segmento_id == segmento_id).first()

    if segmento is not None:
        seg_dict = segmento.as_dict()

        seg_dict['ponto_inicial'] = get_ponto(segmento.ponto_inicial).get('nome')
        seg_dict['ponto_final'] = get_ponto(segmento.ponto_final).get('nome')

        return seg_dict

    return {}


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
        raise InvalidFieldException("segmento")


def put_segmento(segmento: dict[str, str], segmento_id: int) -> Segmento:
    if validate_segmento(segmento):
        existing_segmento = Segmento.query.filter(Segmento.segmento_id == segmento_id).first()
        for key, value in segmento.items():
            setattr(existing_segmento, key, value)
        db.session.commit()
        return existing_segmento
    else:
        raise InvalidFieldException("segmento")


def delete_segmento(segmento_id: int) -> None:
    existing_segmento = Segmento.query.filter(Segmento.segmento_id == segmento_id).first()
    if existing_segmento is not None:
        db.session.delete(existing_segmento)
        db.session.commit()
    else:
        raise InvalidFieldException("id_segmento")
