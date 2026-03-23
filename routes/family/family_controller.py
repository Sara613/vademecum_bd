from flask import request
from .family_service import FamilyService
from common.http import success_response, error_response

class FamilyController:
    @staticmethod
    def get_all():
        families = FamilyService.get_all()
        return success_response([f.to_dict() for f in families])

    @staticmethod
    def get_by_id(family_id):
        family = FamilyService.get_by_id(family_id)
        if family:
            return success_response(family.to_dict())
        return error_response("Familia no encontrada", 404)

    @staticmethod
    def create():
        data = request.json
        if not data or 'name' not in data or 'id_therapeutic_group' not in data:
            return error_response("El nombre y el ID del grupo terapéutico son requeridos", 400)
        try:
            new_family = FamilyService.create(data)
            return success_response(new_family.to_dict(), "Familia creada exitosamente", 201)
        except Exception as e:
            return error_response(str(e), 500)

    @staticmethod
    def update(family_id):
        data = request.json
        family = FamilyService.update(family_id, data)
        if family:
            return success_response(family.to_dict(), "Familia actualizada exitosamente")
        return error_response("Familia no encontrada", 404)

    @staticmethod
    def delete(family_id):
        if FamilyService.delete(family_id):
            return success_response(None, "Familia eliminada exitosamente")
        return error_response("Familia no encontrada", 404)
