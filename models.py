from extensions import db


class Usuario(db.Model):
    __tablename__: str = 'usuario'
    id_usuario: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registro: db.Column = db.Column(db.String, unique=True, index=True)
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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Ponto(db.Model):
    __tablename__: str = 'ponto'
    id_ponto: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome: db.Column = db.Column(db.String, unique=True, index=True)

    def __init__(self, nome) -> None:
        self.nome = nome

    def __repr__(self) -> str:
        return f"<Ponto {self.nome}>"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Segmento(db.Model):
    __tablename__: str = 'segmento'
    id_segmento: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distancia: db.Column = db.Column(db.Integer)
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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}