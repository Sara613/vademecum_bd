from flask import Blueprint
from .therapeutic_controller import TherapeuticController

therapeutic_bp = Blueprint('therapeutic_groups', __name__, url_prefix='/api/therapeutic-groups')

@therapeutic_bp.route('', methods=['GET'])
def get_all():
    return TherapeuticController.get_all()

@therapeutic_bp.route('/<int:group_id>', methods=['GET'])
def get_by_id(group_id):
    return TherapeuticController.get_by_id(group_id)

@therapeutic_bp.route('', methods=['POST'])
def create():
    return TherapeuticController.create()

@therapeutic_bp.route('/<int:group_id>', methods=['PUT'])
def update(group_id):
    return TherapeuticController.update(group_id)

@therapeutic_bp.route('/<int:group_id>', methods=['DELETE'])
def delete(group_id):
    return TherapeuticController.delete(group_id)
