
from fastapi import APIRouter
from src.api.models import MessageResponse, UserInput
from src.nodes.agent.rag.rag_chain import get_rag_chain 

graph_router = APIRouter(prefix="/graph", tags=["Graph Operations"])

@graph_router.get("/message")
async def read_root():
    return {"message": "Welcome to Projeto Nível 3 API!!!"}

 
@graph_router.post("/message", response_model=MessageResponse)
def send_message(input_data: UserInput):
    """Executa o fluxo de IA"""
    # Chama o pipeline RAG para responder com base no PDF
    rag_chain = get_rag_chain()
    resposta = rag_chain.invoke({"question": input_data.input_message})
    if hasattr(resposta, "content"):
        resposta = resposta.content
        return MessageResponse(
            user_input=input_data.input_message,
            output_message=resposta,
            session_id=input_data.session_id
        )  
    