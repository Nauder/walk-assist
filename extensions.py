from werkzeug.exceptions import HTTPException

from flask import Flask, json
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
app_migrate: Migrate = Migrate()
jwt: JWTManager = JWTManager()
flask_app: Flask = Flask(__name__.split('.')[0])


@flask_app.errorhandler(HTTPException)
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
