# Projeto Supa-Z 

Este projeto é um script em Python desenvolvido para buscar contatos armazenados em um banco de dados Supabase e simular o fluxo de disparo de mensagens de forma automatizada.

##Tecnologias Utilizadas

* **Python 3**
* **Supabase** (Banco de dados)
* **Python-dotenv** (Gerenciamento de variáveis de ambiente)


## Pré-requisitos

Antes de iniciar, você vai precisar ter instalado em sua máquina:
* Git
* Python 3.8 ou superior

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
SUPABASE_URL=sua url aqui
SUPABASE_KEY=sua chave aqui
```

### 4. Executar o Script de Teste
Para rodar a simulação do envio de mensagens, execute:
```bash
python main.py
```

## Status do Desenvolvimento

* [x] Integração e busca de dados no Supabase.
* [x] Estruturação da lógica de loop e logs do processo.
* [ ] Conexão com API externa para envio real das mensagens.

