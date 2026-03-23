import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from db.db import db
from sqlalchemy import text

# Import Blueprints
from routes.therapeutic_groups.therapeutic_routes import therapeutic_bp
from routes.family.family_routes import family_bp
from routes.laboratory.laboratory_routes import laboratory_bp
from routes.products.products_routes import products_bp
from routes.pharmaceutical_form.pharmaceutical_form_routes import pharma_form_bp
from routes.posology.posology_routes import posology_bp
from routes.auth.auth_routes import auth_bp

# Load environment variables
load_dotenv()

def sync_sequences():
    """Sincroniza las secuencias de PostgreSQL con el valor máximo de los IDs en cada tabla."""
    tables_to_sync = [
        ('therapeutic_groups', 'id_therapeutic_group'),
        ('family', 'id_family'),
        ('laboratory', 'id_laboratory'),
        ('pharmaceutical_form', 'id_pharmaceutical_form'),
        ('posology', 'id_posology'),
        ('product_details', 'id_product'),
        ('users', 'id')
    ]
    
    for table, column in tables_to_sync:
        try:
            # SQL para actualizar la secuencia al valor máximo actual
            query = f"SELECT setval(pg_get_serial_sequence('{table}', '{column}'), MAX({column})) FROM {table};"
            db.session.execute(text(query))
        except Exception as e:
            # print(f"Error sincronizando secuencia para {table}: {e}")
            db.session.rollback()
    
    db.session.commit()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.url_map.strict_slashes = False

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # JWT Configuration
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'default-secret-key')
    jwt = JWTManager(app)

    # Initialize Database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(therapeutic_bp)
    app.register_blueprint(family_bp)
    app.register_blueprint(laboratory_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(pharma_form_bp)
    app.register_blueprint(posology_bp)
    app.register_blueprint(auth_bp)

    # Create tables if they don't exist and sync sequences
    with app.app_context():
        from db.models import TherapeuticGroup, Family, Laboratory, PharmaceuticalForm, Posology, ProductDetails, User
        db.create_all()
        sync_sequences()

    @app.route('/')
    def index():
        return {"message": "Vademecum API is running"}

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
