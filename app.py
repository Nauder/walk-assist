import os

from flask import Flask, json

from blueprints.login_workshop import login_mold
from blueprints.usuario_workshop import usuario_mold
from extensions import db, app_migrate
from werkzeug.exceptions import HTTPException


def create_app() -> Flask:
    new_app: Flask = Flask(__name__.split('.')[0])
    new_app.config.from_pyfile(os.path.join(".", "config/app.conf"), silent=False)
    _register_blueprints(new_app)
    _register_extensions(new_app)

    return new_app


def _register_blueprints(new_app):
    new_app.register_blueprint(usuario_mold, url_prefix="/usuarios")
    new_app.register_blueprint(login_mold, url_prefix="/")


def _register_extensions(new_app):
    db.init_app(new_app)
    app_migrate.db = db
    app_migrate.init_app(new_app)


app: Flask = create_app()


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "success": False,
        "code": e.code,
        "name": e.name,
        "message": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
    app.run()
