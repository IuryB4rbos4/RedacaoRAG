import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from app import config

# Carrega knowledge base principal
with open(config.DATA_PATH, "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

with open(config.DATA_PATH_COMPETENCIAS, "r", encoding="utf-8") as f:
    competencias_base = json.load(f)

# Inicializa modelo de embeddings
model = SentenceTransformer(config.EMBEDDING_MODEL)

# Carrega índice FAISS
if not os.path.exists(config.INDEX_PATH):
    raise FileNotFoundError("Índice FAISS não encontrado. Execute build_embeddings.py primeiro.")

index = faiss.read_index(str(config.INDEX_PATH))

def retrieve(query: str, top_k: int = 3, tema_filter: str = None, include_competencias: bool = True):
    """
    Retorna resultados similares ao query da knowledge_base 
    e, opcionalmente, adiciona itens da base de competencias.
    """
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(np.array(query_embedding, dtype="float32"), top_k)

    results = []
    seen_ids = set()

    # Resultados da knowledge_base
    for idx in indices[0]:
        if idx < 0 or idx >= len(knowledge_base):
            continue
        item = knowledge_base[idx]
        if tema_filter and item["tema"] != tema_filter:
            continue
        if item["id"] not in seen_ids:
            results.append(item)
            seen_ids.add(item["id"])

    # Adiciona base de competencias sempre que solicitado
    if include_competencias:
        for item in competencias_base:
            if item["id"] not in seen_ids:
                results.append(item)
                seen_ids.add(item["id"])

    return results
