import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from app import config

# Inicializa modelo de embeddings
model = SentenceTransformer(config.EMBEDDING_MODEL)

# Carrega knowledge base
with open(config.DATA_PATH, "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

# Carrega índice FAISS
if not os.path.exists(config.INDEX_PATH):
    raise FileNotFoundError("Índice FAISS não encontrado. Execute build_embeddings.py primeiro.")

index = faiss.read_index(config.INDEX_PATH)

def retrieve(query: str, top_k: int = 3, tema_filter: str = None):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(np.array(query_embedding, dtype="float32"), top_k)

    results = []
    seen_ids = set()
    for idx in indices[0]:
        item = knowledge_base[idx]
        if item["id"] not in seen_ids:
            if tema_filter and item["tema"] != tema_filter:
                continue
            results.append({
                "id": item["id"],
                "tema": item["tema"],
                "tipo": item["tipo"],
                "texto": item["texto"],
                "criterios": item.get("criterios", {}),
                "dicas": item.get("dicas", [])
            })
            seen_ids.add(item["id"])
    return results