from flask_jwt_extended import create_access_token
from common.http import success_response, error_response
from .auth_service import AuthService

class AuthController:
    @staticmethod
    def login_user(data):
        user, err = AuthService.login_user(data)
        if err:
            return error_response(message=err.get("message", "Login Inválido"), status_code=401)
        
        # Identity can be any serializable data, usually user ID
        token = create_access_token(identity=str(user.id))

        return success_response(
            data={
                "access_token": token,
                "user": user.to_dict()
            },
            message="Login exitoso"
        )

    @staticmethod
    def create_user(data):
        user, err = AuthService.create_user(data)
        if err:
            return error_response(message=err.get("message", "No se pudo crear el usuario"), status_code=400)
        
        return success_response(data=user.to_dict(), message="Usuario creado", status_code=201)
