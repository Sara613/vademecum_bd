import os
from dotenv import load_dotenv
from db.mongo import get_mongo_db
 
load_dotenv()
 
COLLECTION_NAME = os.getenv("MONGO_COLLECTION_PRODUCT_IMAGES", "product_images")
 
 
def init_mongo():
    db = get_mongo_db()
 
    validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "product_id",
                "name",
                "image_url",
                "image_type",
                "created_at",
                "updated_at",
            ],
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "product_id": {
                    "bsonType": "int",
                    "minimum": 1
                },
                "name": {
                    "bsonType": "string",
                    "minLength": 2
                },
                "image_url": {
                    "bsonType": "string"
                },
                "image_type": {
                    "enum": ["frontal", "lateral", "etiqueta", "ingredientes", "otra"]
                },
                "created_at": {
                    "bsonType": "date"
                },
                "updated_at": {
                    "bsonType": "date"
                },
            },
            "additionalProperties": False,
        }
    }
 
    collections = db.list_collection_names()
 
    if COLLECTION_NAME not in collections:
        db.create_collection(COLLECTION_NAME, validator=validator)
        print(f"Colección '{COLLECTION_NAME}' creada con validación.")
    else:
        # Actualizar el validador si la colección ya existe
        db.command(
            "collMod",
            COLLECTION_NAME,
            validator=validator,
            validationLevel="moderate",
        )
        print(f"Colección '{COLLECTION_NAME}' ya existe. Validador actualizado.")
 
 
if __name__ == "__main__":
    init_mongo()