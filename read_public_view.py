
from config import get_client, DB_NAME

client = get_client()
db = client[DB_NAME]

try:
    for patient in db.patients_public.find(
        {},
        {"_id": 0}
    ).sort("created_at", -1).limit(10):
        print(patient)

finally:
    client.close()
