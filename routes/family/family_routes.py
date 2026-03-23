from flask import Blueprint
from .family_controller import FamilyController

family_bp = Blueprint('family', __name__, url_prefix='/api/families')

@family_bp.route('', methods=['GET'])
def get_all():
    return FamilyController.get_all()

@family_bp.route('/<int:family_id>', methods=['GET'])
def get_by_id(family_id):
    return FamilyController.get_by_id(family_id)

@family_bp.route('', methods=['POST'])
def create():
    return FamilyController.create()

@family_bp.route('/<int:family_id>', methods=['PUT'])
def update(family_id):
    return FamilyController.update(family_id)

@family_bp.route('/<int:family_id>', methods=['DELETE'])
def delete(family_id):
    return FamilyController.delete(family_id)
