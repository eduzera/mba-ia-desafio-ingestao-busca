# Desafio MBA Engenharia de Software com IA - Full Cycle

## Pre requisitos
- Docker
- Docker Compose

## Como rodar a aplicação
1. Clone este repositório:
   ```bash
    git clone https://github.com/eduzera/mba-ia-desafio-ingestao-busca.git
    
    cd mba-ia-desafio-ingestao-busca
    ``` 

2. Crie e ative um ambiente virtual Python:
   ```bash
    python3 -m venv venv
    
    source venv/bin/activate
   ```

3. Configure o arquivo `.env` com suas credenciais do OpenAI, Gemini e outras configurações fazendo uma cópia do arquivo `.env.example`:
    ```bash
    cp .env.example .env
    ```
    Edite o arquivo `.env` e adicione suas chaves de API e outras configurações necessárias:
    ```
    OPENAI_API_KEY=sua_chave_openai_aqui
    GOOGLE_API_KEY=sua_chave_gemini_aqui
    DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
    PG_VECTOR_COLLECTION_NAME=gpt5_collection
    PDF_PATH=./document.pdf
    ```
4. Construa e inicie os contêineres Docker:
   ```bash
   docker-compose up --build -d
   ``` 

5. Instale as dependências Python:
   ```bash
   pip install -r requirements.txt
   ``` 

## Executando a aplicação

### Ingestão de Documentos PDF
Para ingerir documentos PDF e armazenar os embeddings no banco de dados, execute o seguinte comando:
```bash
python src/ingest.py
```

### Respondendo Perguntas
Para fazer perguntas baseadas nos documentos ingeridos, execute o seguinte comando:
```bash
python src/chat.py
```

Insira sua pergunta quando solicitado. E o sistema retornará uma resposta baseada no conteúdo dos documentos PDF ingeridos. Caso a pergunta não possa ser respondida com base nos documentos, o sistema informará que não há informações suficientes.

- Exemplo caso de sucesso:

<img src="https://p-pnf75vn.b0.n0.cdn.zight.com/items/P8uPYGkA/dd332318-69d0-4dcd-a5e3-f11da676d6f0.gif?source=viewer&v=f543bbae13cf7c847fbb5aaffd64fbcc">

- Exemplo caso de falha:

<img src="https://p-pnf75vn.b0.n0.cdn.zight.com/items/2NuZrlqN/e0a485d3-e586-4243-bdf7-57d1362b5f2a.gif?source=viewer&v=b155b038ef5fb40da7d520011cb77838">