from db.models import TherapeuticGroup
from db.db import db

class TherapeuticService:
    @staticmethod
    def get_all():
        return TherapeuticGroup.query.all()

    @staticmethod
    def get_by_id(group_id):
        return TherapeuticGroup.query.get(group_id)

    @staticmethod
    def create(data):
        new_group = TherapeuticGroup(name=data['name'])
        db.session.add(new_group)
        db.session.commit()
        return new_group

    @staticmethod
    def update(group_id, data):
        group = TherapeuticGroup.query.get(group_id)
        if group:
            group.name = data.get('name', group.name)
            db.session.commit()
        return group

    @staticmethod
    def delete(group_id):
        group = TherapeuticGroup.query.get(group_id)
        if group:
            db.session.delete(group)
            db.session.commit()
            return True
        return False
