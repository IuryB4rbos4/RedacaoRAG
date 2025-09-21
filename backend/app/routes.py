from app.feedback import generate_feedback
from fastapi import APIRouter
from pydantic import BaseModel
from app.retrieval import retrieve as search_similar



router = APIRouter()

class EssayRequest(BaseModel):
    text: str

@router.post("/analyze")
async def analyze_essay(request: EssayRequest):

    contextos = search_similar(request.text)
    feedback = generate_feedback(request.text, contextos)

    return {
        "received_text": request.text,
        "contextos_relevantes": contextos,
        "feedback": feedback
    }