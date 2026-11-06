
from config import get_client, DB_NAME
from datetime import datetime, timezone

client = get_client()
db = client[DB_NAME]

try:
    db.patients.insert_one({
        "full_name": "A",
        "email": "correo_incorrecto",
        "age": 300,
        "created_at": datetime.now(timezone.utc)
    })

    print("Documento aceptado.")

except Exception as e:
    print("Documento rechazado correctamente por la validación.")

finally:
    client.close()
