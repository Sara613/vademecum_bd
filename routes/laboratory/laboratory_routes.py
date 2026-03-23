from flask import Blueprint
from .laboratory_controller import LaboratoryController

laboratory_bp = Blueprint('laboratory', __name__, url_prefix='/api/laboratories')

@laboratory_bp.route('', methods=['GET'])
def get_all():
    return LaboratoryController.get_all()

@laboratory_bp.route('/<int:lab_id>', methods=['GET'])
def get_by_id(lab_id):
    return LaboratoryController.get_by_id(lab_id)

@laboratory_bp.route('', methods=['POST'])
def create():
    return LaboratoryController.create()

@laboratory_bp.route('/<int:lab_id>', methods=['PUT'])
def update(lab_id):
    return LaboratoryController.update(lab_id)

@laboratory_bp.route('/<int:lab_id>', methods=['DELETE'])
def delete(lab_id):
    return LaboratoryController.delete(lab_id)
