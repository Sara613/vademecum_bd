from typing import Any, Tuple, Dict, Optional
from db.db import db
from db.models import User
from werkzeug.security import check_password_hash, generate_password_hash

class AuthService:
    @staticmethod
    def login_user(data: Dict[str, Any]) -> Tuple[Optional[User], Any]:
        identification = data.get("identification", "").strip()
        password = data.get("password", "").strip()

        if not identification or not password:
            return None, {"message": "Cédula y contraseña son requeridas"}
        
        user = User.query.filter(User.identification == identification).first()
        
        if not user:
            return None, {"message": "Usuario no encontrado"}
        if not user.is_active:
            return None, {"message": "Usuario inactivo"}
        if not check_password_hash(user.password_hash, password):
            return None, {"message": "Contraseña incorrecta"}
            
        return user, None

    @staticmethod
    def create_user(data: Dict[str, Any]) -> Tuple[Optional[User], Any]:
        identification = (data.get("identification") or "").strip()
        password = data.get("password") or ""
        full_name = (data.get("full_name") or "").strip()

        if not identification or not password:
            return None, {"message": "Identificación y contraseña son requeridos"}

        exists = User.query.filter(User.identification == identification).first()
        if exists:
            return None, {"message": "Ya existe un usuario con esa identificación"}

        user = User(
            identification=identification,
            full_name=full_name,
            password_hash=generate_password_hash(password)
        )
        
        try:
            db.session.add(user)
            db.session.commit()
            return user, None
        except Exception as e:
            db.session.rollback()
            return None, {"message": str(e)}
