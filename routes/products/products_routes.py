from flask import Blueprint
from .products_controller import ProductController

products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('', methods=['GET'])
def get_all():
    return ProductController.get_all()

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_by_id(product_id):
    return ProductController.get_by_id(product_id)

@products_bp.route('', methods=['POST'])
def create():
    return ProductController.create()

@products_bp.route('/<int:product_id>', methods=['PUT'])
def update(product_id):
    return ProductController.update(product_id)

@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete(product_id):
    return ProductController.delete(product_id)
