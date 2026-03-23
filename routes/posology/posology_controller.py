from flask import request
from .posology_service import PosologyService
from common.http import success_response, error_response

class PosologyController:
    @staticmethod
    def get_all():
        posologies = PosologyService.get_all()
        return success_response([p.to_dict() for p in posologies])

    @staticmethod
    def get_by_id(posology_id):
        posology = PosologyService.get_by_id(posology_id)
        if posology:
            return success_response(posology.to_dict())
        return error_response("Posología no encontrada", 404)

    @staticmethod
    def create():
        data = request.json
        if not data or 'name' not in data:
            return error_response("El nombre es requerido", 400)
        try:
            new_posology = PosologyService.create(data)
            return success_response(new_posology.to_dict(), "Posología creada exitosamente", 201)
        except Exception as e:
            return error_response(str(e), 500)

    @staticmethod
    def update(posology_id):
        data = request.json
        posology = PosologyService.update(posology_id, data)
        if posology:
            return success_response(posology.to_dict(), "Posología actualizada exitosamente")
        return error_response("Posología no encontrada", 404)

    @staticmethod
    def delete(posology_id):
        if PosologyService.delete(posology_id):
            return success_response(None, "Posología eliminada exitosamente")
        return error_response("Posología no encontrada", 404)
