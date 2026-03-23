from .db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identification = db.Column(db.String(50), nullable=False, unique=True)
    full_name = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'identification': self.identification,
            'full_name': self.full_name,
            'is_active': self.is_active
        }

class TherapeuticGroup(db.Model):
    __tablename__ = 'therapeutic_groups'
    id_therapeutic_group = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    
    families = db.relationship('Family', backref='therapeutic_group', lazy=True)

    def to_dict(self):
        return {
            'id_therapeutic_group': self.id_therapeutic_group,
            'name': self.name
        }

class Family(db.Model):
    __tablename__ = 'family'
    id_family = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), nullable=False)
    potential_illness = db.Column(db.Text)
    id_therapeutic_group = db.Column(db.Integer, db.ForeignKey('therapeutic_groups.id_therapeutic_group'), nullable=False)
    
    products = db.relationship('ProductDetails', backref='family', lazy=True)

    def to_dict(self):
        return {
            'id_family': self.id_family,
            'name': self.name,
            'potential_illness': self.potential_illness,
            'id_therapeutic_group': self.id_therapeutic_group
        }

class Laboratory(db.Model):
    __tablename__ = 'laboratory'
    id_laboratory = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    
    products = db.relationship('ProductDetails', backref='laboratory', lazy=True)

    def to_dict(self):
        return {
            'id_laboratory': self.id_laboratory,
            'name': self.name
        }

class PharmaceuticalForm(db.Model):
    __tablename__ = 'pharmaceutical_form'
    id_pharmaceutical_form = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    
    products = db.relationship('ProductDetails', backref='pharmaceutical_form', lazy=True)

    def to_dict(self):
        return {
            'id_pharmaceutical_form': self.id_pharmaceutical_form,
            'name': self.name
        }

class Posology(db.Model):
    __tablename__ = 'posology'
    id_posology = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    
    products = db.relationship('ProductDetails', backref='posology', lazy=True)

    def to_dict(self):
        return {
            'id_posology': self.id_posology,
            'name': self.name
        }

class ProductDetails(db.Model):
    __tablename__ = 'product_details'
    id_product = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commercial_name = db.Column(db.String(200), nullable=False)
    generic_name = db.Column(db.String(200))
    id_family = db.Column(db.Integer, db.ForeignKey('family.id_family'))
    action_mechanism = db.Column(db.Text)
    id_laboratory = db.Column(db.Integer, db.ForeignKey('laboratory.id_laboratory'))
    concentration = db.Column(db.String(50))
    id_pharmaceutical_form = db.Column(db.Integer, db.ForeignKey('pharmaceutical_form.id_pharmaceutical_form'))
    id_posology = db.Column(db.Integer, db.ForeignKey('posology.id_posology'))
    notes = db.Column(db.Text)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def to_dict(self):
        return {
            'id_product': self.id_product,
            'commercial_name': self.commercial_name,
            'generic_name': self.generic_name,
            'id_family': self.id_family,
            'action_mechanism': self.action_mechanism,
            'id_laboratory': self.id_laboratory,
            'concentration': self.concentration,
            'id_pharmaceutical_form': self.id_pharmaceutical_form,
            'id_posology': self.id_posology,
            'notes': self.notes,
            'is_active': self.is_active
        }
