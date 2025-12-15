from pydantic import BaseModel

class UserInput(BaseModel):
    input_message: str
    session_id: str


class MessageResponse(BaseModel):
    user_input: str
    output_message: str
    # input_guardrail: inputGuardrail
    session_id: str
    output_guardrail: str = "N/A"
    rag_agent: str = "N/A"
    fallback: bool = False
    rag_agent_string: list = []
    handover: bool = False 