
from config import get_client, DB_NAME
from pymongo.encryption import ClientEncryption
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.codec_options import CodecOptions
from bson.binary import UuidRepresentation
from dotenv import load_dotenv
import os

load_dotenv()

client = get_client()
key_vault_namespace = f"{DB_NAME}.__keyVault"

kms_providers = {
    "local": {
        "key": open("master-key.bin", "rb").read()
    }
}

encryption = ClientEncryption(
    kms_providers,
    key_vault_namespace,
    client,
    CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
)

try:
    data_key_id = encryption.create_data_key(
        "local",
        key_alt_names=["patients-data-key"]
    )

    print("Llave creada correctamente.")
    print("DATA_KEY_ID:", data_key_id)

finally:
    encryption.close()
    client.close()
