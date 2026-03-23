from flask import Blueprint
from .posology_controller import PosologyController

posology_bp = Blueprint('posology', __name__, url_prefix='/api/posologies')

@posology_bp.route('', methods=['GET'])
def get_all():
    return PosologyController.get_all()

@posology_bp.route('/<int:posology_id>', methods=['GET'])
def get_by_id(posology_id):
    return PosologyController.get_by_id(posology_id)

@posology_bp.route('', methods=['POST'])
def create():
    return PosologyController.create()

@posology_bp.route('/<int:posology_id>', methods=['PUT'])
def update(posology_id):
    return PosologyController.update(posology_id)

@posology_bp.route('/<int:posology_id>', methods=['DELETE'])
def delete(posology_id):
    return PosologyController.delete(posology_id)
