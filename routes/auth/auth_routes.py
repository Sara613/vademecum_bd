from flask import Blueprint, request
from .auth_controller import AuthController

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/create", methods=["POST"])
def create_user():
    return AuthController.create_user(request.get_json() or {})

@auth_bp.route("/login", methods=["POST"])
def login_user():
    return AuthController.login_user(request.get_json() or {})
