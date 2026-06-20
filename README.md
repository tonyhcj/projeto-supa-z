# Projeto Supa-Z 

Esse projeto é um bot simples de disparo de mensagens via WhatsApp (Z-API) integrado com o Supabase como banco de dados.

##Tecnologias Utilizadas

* **Python 3**
* **Supabase** (Banco de dados)
* **Python-dotenv** (Gerenciamento de variáveis de ambiente)
* **Z-API** (WhatsApp API)
* **Request** (Chamadas HTTP)
* **logging** (Monitoramento)

## Pré-requisitos

Antes de iniciar, você vai precisar ter instalado em sua máquina:
* Git
* Python 3.8 ou superior

Para o Supabase é necessario ter:
* Projeto criado 
* Tabela contatos com id, nome e telefone

Para o Z-API é necessario ter: 
* Instância configurada, sem a camada de segurança do contrario é necssesario cabeçalho 

## Como Configurar e Executar o Projeto

### 1. Configurar o ambiente virtual (Recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
```

### 2. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar as Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do projeto e adicione as suas credenciais do Supabase:

```env
SUPABASE_URL=(sua url aqui)
SUPABASE_KEY=(sua chave aqui)


ZAPI_INSTANCE_ID=(id da sua instancia)
ZAPI_TOKEN=(seu token) 

```

### 4. Executar o Script de Teste
Para executar o envio de mensagens:
```bash
python main.py
```


