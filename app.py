import os

from flask import Flask, json
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from blueprints.login_workshop import login_mold
from blueprints.ponto_workshop import ponto_mold
from blueprints.usuario_workshop import usuario_mold
from extensions import db, app_migrate
from services.token_service import jwt


def create_app():
    flask_app: Flask = Flask(__name__.split('.')[0])
    flask_app.config.from_pyfile(os.path.join(".", "config/app.conf"), silent=False)
    _register_blueprints(flask_app)
    _register_extensions(flask_app)
    CORS(flask_app, support_credentials=True)

    return flask_app


def _register_blueprints(flask_app):
    flask_app.register_blueprint(usuario_mold, url_prefix="/usuarios")
    flask_app.register_blueprint(ponto_mold, url_prefix="/pontos")
    flask_app.register_blueprint(login_mold, url_prefix="/")


def _register_extensions(flask_app):
    db.init_app(flask_app)
    jwt.init_app(flask_app)
    app_migrate.db = db
    app_migrate.init_app(flask_app)


app = create_app()


@app.errorhandler(HTTPException)
def _handle_exception(e):
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
    app.run(host="0.0.0.0", port=25000)
