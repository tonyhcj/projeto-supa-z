from supabase_client import get_contatos
from zapi_client import enviar_mensagem
import logging

logging.basicConfig(
    filename="message.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    contatos = get_contatos()

    if not contatos:
        logging.warning("Nenhum contato encontrado.")
        return

    for c in contatos:
        nome = c["nome"]
        telefone = c["telefone"]

        mensagem = f"Olá, {nome} tudo bem com você?"

        status, resp = enviar_mensagem(telefone, mensagem)

        logging.info(f"Enviado para {nome} ({telefone}) | status={status}")

if __name__ == "__main__":
    main()
