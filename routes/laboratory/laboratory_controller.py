from flask import request
from .laboratory_service import LaboratoryService
from common.http import success_response, error_response

class LaboratoryController:
    @staticmethod
    def get_all():
        labs = LaboratoryService.get_all()
        return success_response([l.to_dict() for l in labs])

    @staticmethod
    def get_by_id(lab_id):
        lab = LaboratoryService.get_by_id(lab_id)
        if lab:
            return success_response(lab.to_dict())
        return error_response("Laboratorio no encontrado", 404)

    @staticmethod
    def create():
        data = request.json
        if not data or 'name' not in data:
            return error_response("El nombre es requerido", 400)
        try:
            new_lab = LaboratoryService.create(data)
            return success_response(new_lab.to_dict(), "Laboratorio creado exitosamente", 201)
        except Exception as e:
            return error_response(str(e), 500)

    @staticmethod
    def update(lab_id):
        data = request.json
        lab = LaboratoryService.update(lab_id, data)
        if lab:
            return success_response(lab.to_dict(), "Laboratorio actualizado exitosamente")
        return error_response("Laboratorio no encontrado", 404)

    @staticmethod
    def delete(lab_id):
        if LaboratoryService.delete(lab_id):
            return success_response(None, "Laboratorio eliminado exitosamente")
        return error_response("Laboratorio no encontrado", 404)
