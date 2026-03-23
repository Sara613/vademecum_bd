from db.models import ProductDetails
from db.db import db

class ProductService:
    @staticmethod
    def get_all():
        return ProductDetails.query.all()

    @staticmethod
    def get_by_id(product_id):
        return ProductDetails.query.get(product_id)

    @staticmethod
    def create(data):
        new_product = ProductDetails(
            commercial_name=data['commercial_name'],
            generic_name=data.get('generic_name'),
            id_family=data.get('id_family'),
            action_mechanism=data.get('action_mechanism'),
            id_laboratory=data.get('id_laboratory'),
            concentration=data.get('concentration'),
            id_pharmaceutical_form=data.get('id_pharmaceutical_form'),
            id_posology=data.get('id_posology'),
            notes=data.get('notes'),
            is_active=data.get('is_active', True)
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def update(product_id, data):
        product = ProductDetails.query.get(product_id)
        if product:
            product.commercial_name = data.get('commercial_name', product.commercial_name)
            product.generic_name = data.get('generic_name', product.generic_name)
            product.id_family = data.get('id_family', product.id_family)
            product.action_mechanism = data.get('action_mechanism', product.action_mechanism)
            product.id_laboratory = data.get('id_laboratory', product.id_laboratory)
            product.concentration = data.get('concentration', product.concentration)
            product.id_pharmaceutical_form = data.get('id_pharmaceutical_form', product.id_pharmaceutical_form)
            product.id_posology = data.get('id_posology', product.id_posology)
            product.notes = data.get('notes', product.notes)
            product.is_active = data.get('is_active', product.is_active)
            db.session.commit()
        return product

    @staticmethod
    def delete(product_id):
        product = ProductDetails.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
