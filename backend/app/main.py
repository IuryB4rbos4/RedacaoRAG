from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Redação RAG")

# Inclui rotas
app.include_router(router)