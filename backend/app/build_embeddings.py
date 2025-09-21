import os
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import config

# Cria diretório do índice se não existir
os.makedirs(os.path.dirname(config.INDEX_PATH), exist_ok=True)

# Carrega knowledge base
with open(config.DATA_PATH, "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

# Inicializa modelo de embeddings
model = SentenceTransformer(config.EMBEDDING_MODEL)

# Cria embeddings
texts = [item["texto"] for item in knowledge_base]
embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=True)

# Inicializa índice FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings, dtype="float32"))

# Salva índice
faiss.write_index(index, str(config.INDEX_PATH))

print("Índice FAISS criado com sucesso!")