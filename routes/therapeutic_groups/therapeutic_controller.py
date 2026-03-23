from flask import request
from .therapeutic_service import TherapeuticService
from common.http import success_response, error_response

class TherapeuticController:
    @staticmethod
    def get_all():
        groups = TherapeuticService.get_all()
        return success_response([g.to_dict() for g in groups])

    @staticmethod
    def get_by_id(group_id):
        group = TherapeuticService.get_by_id(group_id)
        if group:
            return success_response(group.to_dict())
        return error_response("Grupo terapéutico no encontrado", 404)

    @staticmethod
    def create():
        data = request.json
        if not data or 'name' not in data:
            return error_response("El nombre es requerido", 400)
        try:
            new_group = TherapeuticService.create(data)
            return success_response(new_group.to_dict(), "Grupo creado exitosamente", 201)
        except Exception as e:
            return error_response(str(e), 500)

    @staticmethod
    def update(group_id):
        data = request.json
        group = TherapeuticService.update(group_id, data)
        if group:
            return success_response(group.to_dict(), "Grupo actualizado exitosamente")
        return error_response("Grupo terapéutico no encontrado", 404)

    @staticmethod
    def delete(group_id):
        if TherapeuticService.delete(group_id):
            return success_response(None, "Grupo eliminado exitosamente")
        return error_response("Grupo terapéutico no encontrado", 404)
