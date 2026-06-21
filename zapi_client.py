import requests
import os
from dotenv import load_dotenv

load_dotenv()

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT = os.getenv("ZAPI_CLIENT")

if not INSTANCE_ID or not TOKEN or not CLIENT:
    raise Exception("Variáveis da Z-API não encontradas no .env")

BASE_URL = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}"

def enviar_mensagem(telefone, mensagem):
    url = f"{BASE_URL}/send-text"

    headers = {
        "Client-Token": CLIENT,
        "Content-Type": "application/json"
    }

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
