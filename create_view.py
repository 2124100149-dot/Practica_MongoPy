
from config import get_client, DB_NAME

client = get_client()
db = client[DB_NAME]

try:
    db.command({
        "create": "patients_public",
        "viewOn": "patients",
        "pipeline": [
            {
                "$project": {
                    "_id": 1,
                    "full_name": 1,
                    "email": 1,
                    "age": 1,
                    "created_at": 1
                }
            }
        ]
    })

    print("Vista pública creada correctamente.")

except Exception as e:
    print("Error:", e)

finally:
    client.close()
