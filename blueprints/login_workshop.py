from flask import Blueprint, request, Response

from exceptions.InvalidCredentialsException import InvalidCredentialsException
from exceptions.InvalidFieldException import InvalidFieldException
from security.login_manager import admin_login_required
from services.usuario_service import get_usuarios, post_usuario, get_usuario, put_usuario, delete_usuario
from util.response_builder import build_response

login_mold = Blueprint("login", __name__)


@login_mold.post('/logon')
def logon_route():
    pass
