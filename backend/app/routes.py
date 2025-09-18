from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EssayRequest(BaseModel):
    text: str

@router.post("/analyze")
async def analyze_essay(request: EssayRequest):
    return {"received_text": request.text, "feedback": "Em breve análise RAG"}
