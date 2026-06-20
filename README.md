# Projeto Supa-Z

Esse projeto é um bot simples de disparo de mensagens via WhatsApp (Z-API) integrado com o Supabase como banco de dados.

###Setup da Tabela no Supabase

Para que o script funcione, você precisa criar uma tabela chamada `contatos` no editor SQL do seu Supabase. Execute o comando abaixo:

```sql
create table contatos (
  id bigint generated always as identity primary key,
  nome text not null,
  telefone text not null
);
```
### Configuração da Z-API
* Configurada sem a camada de segurança extra (caso contrário, será necessário passar cabeçalhos adicionais de segurança no código).

## Como Configurar e Executar o Projeto

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar as Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto e adicione as suas credenciais:

```env
SUPABASE_URL=(seu url do supabase)
SUPABASE_KEY= (sua chave)

ZAPI_INSTANCE_ID=(seu id de instancia z-api)
ZAPI_TOKEN=(seu token)
```

### 4. Executar o Script de Teste

Execute com:

```bash
python3 main.py
```

> **historico:** Por padrão os logs são registrados em `message.log`. Para alterar o comportamento e observar os logs no **terminal**, remova o parâmetro `filename="message.log",` no início do arquivo `main.py`.

> **limite:** Por padrão, o script busca até **3 contatos** cadastrados considerando os mais recentes. Para alterar esse comportamento, modifique o parâmetro `limit` na função `get_contatos()` dentro de `supabase_client.py`.
