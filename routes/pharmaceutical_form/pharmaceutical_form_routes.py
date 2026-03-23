from flask import Blueprint
from .pharmaceutical_form_controller import PharmaceuticalFormController

pharma_form_bp = Blueprint('pharmaceutical_form', __name__, url_prefix='/api/pharmaceutical-forms')

@pharma_form_bp.route('', methods=['GET'])
def get_all():
    return PharmaceuticalFormController.get_all()

@pharma_form_bp.route('/<int:form_id>', methods=['GET'])
def get_by_id(form_id):
    return PharmaceuticalFormController.get_by_id(form_id)

@pharma_form_bp.route('', methods=['POST'])
def create():
    return PharmaceuticalFormController.create()

@pharma_form_bp.route('/<int:form_id>', methods=['PUT'])
def update(form_id):
    return PharmaceuticalFormController.update(form_id)

@pharma_form_bp.route('/<int:form_id>', methods=['DELETE'])
def delete(form_id):
    return PharmaceuticalFormController.delete(form_id)
