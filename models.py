from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.ddl import CreateColumn

from extensions import db


class Usuario(db.Model):
    __tablename__: str = 'usuario'
    id_usuario: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registro: db.Column = db.Column(db.Integer, unique=True, index=True)
    email: db.Column = db.Column(db.String(64), unique=True, index=True)
    senha: db.Column = db.Column(db.String(128))
    nome: db.Column = db.Column(db.String(128))
    tipo_usuario: db.Column = db.Column(db.Integer)

    def __init__(self, registro, email, senha, nome, tipo_usuario) -> None:
        self.registro = registro
        self.email = email
        self.senha = senha
        self.nome = nome
        self.tipo_usuario = tipo_usuario

    def __repr__(self) -> str:
        return f"<Usuario {self.nome}>"

    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Ponto(db.Model):
    __tablename__: str = 'ponto'
    ponto_id: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome: db.Column = db.Column(db.String, unique=True, index=True)

    def __init__(self, nome) -> None:
        self.nome = nome

    def __repr__(self) -> str:
        return f"<Ponto {self.nome}>"

    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Segmento(db.Model):
    __tablename__: str = 'segmento'
    segmento_id: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distancia: db.Column = db.Column(db.Float)
    ponto_inicial: db.Column = db.Column(db.Integer)
    ponto_final: db.Column = db.Column(db.Integer)
    status: db.Column = db.Column(db.Integer)
    direcao: db.Column = db.Column(db.String(128))

    def __init__(self, distancia, ponto_inicial, ponto_final, status, direcao) -> None:
        self.distancia = distancia
        self.ponto_inicial = ponto_inicial
        self.ponto_final = ponto_final
        self.status = status
        self.direcao = direcao

    def __repr__(self) -> str:
        return f"<Segmento {self.nome}>"

    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Session(db.Model):
    __tablename__: str = 'session'
    id_session: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registro: db.Column = db.Column(db.Integer)
    email: db.Column = db.Column(db.String(64))
    nome: db.Column = db.Column(db.String(128))
    tipo_usuario: db.Column = db.Column(db.String(64))

    def __init__(self, registro, email, nome, tipo_usuario) -> None:
        self.registro = registro
        self.email = email
        self.nome = nome
        self.tipo_usuario = tipo_usuario

    def __repr__(self) -> str:
        return f"<Session {self.nome}>"

    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@compiles(CreateColumn, 'postgresql')
def use_identity(element, compiler, **kw):
    text = compiler.visit_create_column(element, **kw)
    text = text.replace("SERIAL", "INT GENERATED BY DEFAULT AS IDENTITY")
    return text
