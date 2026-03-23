from db.models import Family
from db.db import db

class FamilyService:
    @staticmethod
    def get_all():
        return Family.query.all()

    @staticmethod
    def get_by_id(family_id):
        return Family.query.get(family_id)

    @staticmethod
    def create(data):
        new_family = Family(
            name=data['name'],
            potential_illness=data.get('potential_illness'),
            id_therapeutic_group=data['id_therapeutic_group']
        )
        db.session.add(new_family)
        db.session.commit()
        return new_family

    @staticmethod
    def update(family_id, data):
        family = Family.query.get(family_id)
        if family:
            family.name = data.get('name', family.name)
            family.potential_illness = data.get('potential_illness', family.potential_illness)
            family.id_therapeutic_group = data.get('id_therapeutic_group', family.id_therapeutic_group)
            db.session.commit()
        return family

    @staticmethod
    def delete(family_id):
        family = Family.query.get(family_id)
        if family:
            db.session.delete(family)
            db.session.commit()
            return True
        return False
