import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Chaves e Configurações
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Caminhos importantes
INDEX_PATH = "embeddings-db/index/faiss.index"
DATA_PATH = "backend/app/knowledge_base.json"

# Configurações gerais
EMBEDDING_MODEL = "text-embedding-3-small"
TOP_K_RESULTS = 3  # número de documentos a recuperar