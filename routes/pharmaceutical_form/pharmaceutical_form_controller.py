from flask import request
from .pharmaceutical_form_service import PharmaceuticalFormService
from common.http import success_response, error_response

class PharmaceuticalFormController:
    @staticmethod
    def get_all():
        forms = PharmaceuticalFormService.get_all()
        return success_response([f.to_dict() for f in forms])

    @staticmethod
    def get_by_id(form_id):
        form = PharmaceuticalFormService.get_by_id(form_id)
        if form:
            return success_response(form.to_dict())
        return error_response("Forma farmacéutica no encontrada", 404)

    @staticmethod
    def create():
        data = request.json
        if not data or 'name' not in data:
            return error_response("El nombre es requerido", 400)
        try:
            new_form = PharmaceuticalFormService.create(data)
            return success_response(new_form.to_dict(), "Forma farmacéutica creada exitosamente", 201)
        except Exception as e:
            return error_response(str(e), 500)

    @staticmethod
    def update(form_id):
        data = request.json
        form = PharmaceuticalFormService.update(form_id, data)
        if form:
            return success_response(form.to_dict(), "Forma farmacéutica actualizada exitosamente")
        return error_response("Forma farmacéutica no encontrada", 404)

    @staticmethod
    def delete(form_id):
        if PharmaceuticalFormService.delete(form_id):
            return success_response(None, "Forma farmacéutica eliminada exitosamente")
        return error_response("Forma farmacéutica no encontrada", 404)
