from flask import request
from .products_service import ProductService
from common.http import success_response, error_response

class ProductController:
    @staticmethod
    def get_all():
        products = ProductService.get_all()
        return success_response([p.to_dict() for p in products])

    @staticmethod
    def get_by_id(product_id):
        product = ProductService.get_by_id(product_id)
        if product:
            return success_response(product.to_dict())
        return error_response("Producto no encontrado", 404)

    @staticmethod
    def create():
        data = request.json
        if not data or 'commercial_name' not in data:
            return error_response("El nombre comercial es requerido", 400)
        try:
            new_product = ProductService.create(data)
            return success_response(new_product.to_dict(), "Producto creado exitosamente", 201)
        except Exception as e:
            return error_response(str(e), 500)

    @staticmethod
    def update(product_id):
        data = request.json
        product = ProductService.update(product_id, data)
        if product:
            return success_response(product.to_dict(), "Producto actualizado exitosamente")
        return error_response("Producto no encontrado", 404)

    @staticmethod
    def delete(product_id):
        if ProductService.delete(product_id):
            return success_response(None, "Producto eliminado exitosamente")
        return error_response("Producto no encontrado", 404)
