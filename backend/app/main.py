from fastapi import FastAPI
from app.routes import router as retrieval_router

app = FastAPI(title="RedacaoRAG API")
app.include_router(retrieval_router)