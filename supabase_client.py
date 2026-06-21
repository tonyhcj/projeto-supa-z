from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv() 

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise Exception("Variáveis SUPABASE_URL ou SUPABASE_KEY não encontradas no .env")

supabase = create_client(url, key)

def get_contatos(limit=3):
    response = supabase.table("contatos").select("*").order("id",desc=True).limit(limit).execute()
    return response.data
