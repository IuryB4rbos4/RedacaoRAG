from app import config
from google import genai

client = genai.Client(api_key=config.GOOGLE_API_KEY)

def generate_feedback(user_text: str, contextos: list):
    """
    Recebe o texto do usuário e os contextos recuperados pelo RAG.
    Retorna feedback gerado pela LLM.
    """
    context_text = "\n".join([c["texto"] for c in contextos])
    
    prompt = f"""
    Você é um professor avaliador de redações. 
    Texto do aluno:
    {user_text}

    Contextos relevantes da base de conhecimento:
    {context_text}

    Com base nos contextos, forneça feedback detalhado sobre a redação,
    incluindo pontos fortes e sugestões de melhoria.
    também inclua a possível pontuação do texto apresentado, de zero a 1000 e com base nas competencias da base de conhecimento
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.candidates[0].content.parts[0].text