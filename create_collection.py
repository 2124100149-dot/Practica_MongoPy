
from config import get_client, DB_NAME

client = get_client()
db = client[DB_NAME]

schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "full_name",
            "email",
            "national_id",
            "diagnosis",
            "created_at"
        ],
        "properties": {
            "full_name": {
                "bsonType": "string",
                "minLength": 3,
                "maxLength": 120
            },
            "email": {
                "bsonType": "string",
                "pattern": "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"
            },
            "national_id": {
                "bsonType": "binData"
            },
            "diagnosis": {
                "bsonType": "binData"
            },
            "age": {
                "bsonType": "int",
                "minimum": 0,
                "maximum": 120
            },
            "created_at": {
                "bsonType": "date"
            }
        }
    }
}

try:
    if "patients" in db.list_collection_names():
        print("La colección patients ya existe.")
    else:
        db.create_collection(
            "patients",
            validator=schema,
            validationLevel="strict",
            validationAction="error"
        )
        print("Colección patients creada correctamente.")

finally:
    client.close()
