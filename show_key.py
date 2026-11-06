import uuid
from config import get_client, DB_NAME
from bson.codec_options import CodecOptions
from bson.binary import UuidRepresentation
from pymongo.encryption import ClientEncryption

client = get_client()

encryption = ClientEncryption(
    {"local": {"key": open("master-key.bin", "rb").read()}},
    f"{DB_NAME}.__keyVault",
    client,
    CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
)

try:
    key = encryption.get_key_by_alt_name("patients-data-key")
    print(uuid.UUID(bytes=key["_id"]))
finally:
    encryption.close()
    client.close()