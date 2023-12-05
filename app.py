import os
from logging.config import dictConfig

from flask import Flask, json, request, Response
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from blueprints.login_workshop import login_mold
from blueprints.ponto_workshop import ponto_mold
from blueprints.rota_workshop import rota_mold
from blueprints.segmento_workshop import segmento_mold
from blueprints.usuario_workshop import usuario_mold
from extensions import db, app_migrate
from services.token_service import jwt


def create_app():
    """
    Creates and configures a Flask application instance.

    Returns:
        Flask: The configured Flask application instance.
    """

    _configure_logger()
    flask_app: Flask = Flask(__name__.split('.')[0])
    flask_app.config.from_pyfile(os.path.join(".", "config/app.conf"), silent=False)
    _register_blueprints(flask_app)
    _register_extensions(flask_app)
    CORS(flask_app, support_credentials=True)

    return flask_app


def _register_blueprints(flask_app):
    flask_app.register_blueprint(usuario_mold, url_prefix="/usuarios")
    flask_app.register_blueprint(ponto_mold, url_prefix="/pontos")
    flask_app.register_blueprint(segmento_mold, url_prefix="/segmentos")
    flask_app.register_blueprint(login_mold, url_prefix="/")
    flask_app.register_blueprint(rota_mold, url_prefix="/rotas")


def _register_extensions(flask_app):
    db.init_app(flask_app)
    jwt.init_app(flask_app)
    app_migrate.db = db
    app_migrate.init_app(flask_app)


def _configure_logger():
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
                    "datefmt": "%d/%m/%Y %H:%M:%S",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                },
            },
            "root": {"level": "DEBUG", "handlers": ["console"]},
        }
    )


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


@app.before_request
def log_request_info() -> None:
    app.logger.debug(f'REQUEST [{request.path}] <<')
    app.logger.debug(f'Headers:\n{request.headers}')
    app.logger.debug(f'Body:\n{request.get_data()}')


@app.after_request
def log_request_info(response: Response) -> Response:
    app.logger.debug('RESPONSE >>')
    app.logger.debug(f'Headers:\n{response.headers}')
    app.logger.debug(f'Body:\n{response.get_data()}')

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=22000)
