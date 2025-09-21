FROM python:3.11-slim

WORKDIR /app

# Copia e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia a aplicação
COPY ./app ./app
COPY ./embeddings-db ./embeddings-db
COPY ./app/knowledge_base.json ./app/knowledge_base.json

# Gera embeddings durante o build
RUN python3 ./app/build_embeddings.py

# Expondo porta
EXPOSE 8000

# Inicia FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]