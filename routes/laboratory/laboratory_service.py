from db.models import Laboratory
from db.db import db

class LaboratoryService:
    @staticmethod
    def get_all():
        return Laboratory.query.all()

    @staticmethod
    def get_by_id(lab_id):
        return Laboratory.query.get(lab_id)

    @staticmethod
    def create(data):
        new_lab = Laboratory(name=data['name'])
        db.session.add(new_lab)
        db.session.commit()
        return new_lab

    @staticmethod
    def update(lab_id, data):
        lab = Laboratory.query.get(lab_id)
        if lab:
            lab.name = data.get('name', lab.name)
            db.session.commit()
        return lab

    @staticmethod
    def delete(lab_id):
        lab = Laboratory.query.get(lab_id)
        if lab:
            db.session.delete(lab)
            db.session.commit()
            return True
        return False
