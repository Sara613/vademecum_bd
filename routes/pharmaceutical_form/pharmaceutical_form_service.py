from db.models import PharmaceuticalForm
from db.db import db

class PharmaceuticalFormService:
    @staticmethod
    def get_all():
        return PharmaceuticalForm.query.all()

    @staticmethod
    def get_by_id(form_id):
        return PharmaceuticalForm.query.get(form_id)

    @staticmethod
    def create(data):
        new_form = PharmaceuticalForm(name=data['name'])
        db.session.add(new_form)
        db.session.commit()
        return new_form

    @staticmethod
    def update(form_id, data):
        form = PharmaceuticalForm.query.get(form_id)
        if form:
            form.name = data.get('name', form.name)
            db.session.commit()
        return form

    @staticmethod
    def delete(form_id):
        form = PharmaceuticalForm.query.get(form_id)
        if form:
            db.session.delete(form)
            db.session.commit()
            return True
        return False
