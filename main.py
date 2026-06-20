from supabase_client import get_contatos
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    contatos = get_contatos(limit=3)

    if not contatos:
        logging.warning("Nenhum contato encontrado.")
        return

    for c in contatos:
        nome = c["nome"]
        telefone = c["telefone"]

        mensagem = f"Olá, {nome} tudo bem com você?"
        logging.info(f" (Testando processo) Enviaria para {nome} ({telefone}) -> {mensagem}")

if __name__ == "__main__":
    main()
