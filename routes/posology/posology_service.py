from db.models import Posology
from db.db import db

class PosologyService:
    @staticmethod
    def get_all():
        return Posology.query.all()

    @staticmethod
    def get_by_id(posology_id):
        return Posology.query.get(posology_id)

    @staticmethod
    def create(data):
        new_posology = Posology(name=data['name'])
        db.session.add(new_posology)
        db.session.commit()
        return new_posology

    @staticmethod
    def update(posology_id, data):
        posology = Posology.query.get(posology_id)
        if posology:
            posology.name = data.get('name', posology.name)
            db.session.commit()
        return posology

    @staticmethod
    def delete(posology_id):
        posology = Posology.query.get(posology_id)
        if posology:
            db.session.delete(posology)
            db.session.commit()
            return True
        return False
