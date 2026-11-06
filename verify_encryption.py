
from config import get_client, DB_NAME

client = get_client()
db = client[DB_NAME]

try:
    patient = db.patients.find_one({"full_name": "Ana López"})
    print(patient)
finally:
    client.close()
