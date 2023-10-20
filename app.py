import os

from flask import Flask

from blueprints.login_workshop import login_mold
from blueprints.ponto_workshop import ponto_mold
from blueprints.usuario_workshop import usuario_mold
from extensions import db, app_migrate, jwt, flask_app


class AppWrapper:
    app: Flask = flask_app

    def __init__(self):
        self.app.config.from_pyfile(os.path.join(".", "config/app.conf"), silent=False)
        self._register_blueprints()
        self._register_extensions()

    def _register_blueprints(self):
        self.app.register_blueprint(usuario_mold, url_prefix="/usuarios")
        self.app.register_blueprint(ponto_mold, url_prefix="/pontos")
        self.app.register_blueprint(login_mold, url_prefix="/")

    def _register_extensions(self):
        db.init_app(self.app)
        jwt.init_app(self.app)
        app_migrate.db = db
        app_migrate.init_app(self.app)


if __name__ == '__main__':
    app_wrapper = AppWrapper()
    app_wrapper.app.run(host="0.0.0.0")
