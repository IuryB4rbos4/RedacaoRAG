import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "knowledge_base.json"
DATA_PATH_COMPETENCIAS = BASE_DIR / "competencias_base.json"
INDEX_PATH = BASE_DIR / "embeddings-db/index/faiss.index"
GOOGLE_API_KEY=""
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
