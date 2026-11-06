
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from pymongo.encryption import ClientEncryption
from pymongo.encryption import Algorithm
from pymongo import MongoClient
from bson.codec_options import CodecOptions
from bson.binary import UuidRepresentation
from config import get_client, DB_NAME

load_dotenv()

client = get_client()
db = client[DB_NAME]

kms_providers = {
    "local": {
        "key": open("master-key.bin", "rb").read()
    }
}

key_vault_namespace = f"{DB_NAME}.__keyVault"

encryption = ClientEncryption(
    kms_providers,
    key_vault_namespace,
    client,
    CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
)

key_id = encryption.get_key_by_alt_name(
    "patients-data-key"
)["_id"]

try:
    patient = {
        "full_name": "Ana López",
        "email": "ana.lopez@example.com",
        "age": 34,
        "national_id": encryption.encrypt(
            "CURP-123456HDFRRS09",
            Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
            key_id
        ),
        "diagnosis": encryption.encrypt(
            "Hipertensión controlada",
            Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Random,
            key_id
        ),
        "created_at": datetime.now(timezone.utc)
    }

    db.patients.insert_one(patient)
    print("Paciente insertado correctamente.")

finally:
    encryption.close()
    client.close()
