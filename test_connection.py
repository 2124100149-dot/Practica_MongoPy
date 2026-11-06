
from config import get_client

client = get_client()

try:
    client.admin.command("ping")
    print("¡Conexión exitosa con MongoDB Atlas!")
except Exception as e:
    print("Error al conectar:")
    print(e)
finally:
    client.close()
