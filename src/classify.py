import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def classify_message(message, model_id=None):
    """
    Classifica uma mensagem usando o modelo fine-tuned
    
    Args:
        message: Texto da mensagem a ser classificada
        model_id: ID do modelo fine-tuned (se None, usa gpt-3.5-turbo padrão)
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Se não tiver modelo fine-tuned, usa o modelo base
    model = model_id if model_id else "gpt-3.5-turbo"
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente que classifica mensagens de clientes em 'venda' ou 'suporte'. Responda apenas com 'venda' ou 'suporte'."
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=0,
        max_tokens=10
    )
    
    return response.choices[0].message.content.strip().lower()

def main():
    # Teste com mensagens de exemplo
    test_messages = [
        "Quero comprar um notebook",
        "Meu produto está com defeito",
        "Gostaria de adquirir a TV Smart",
        "Como faço para trocar?"
    ]
    
    for msg in test_messages:
        category = classify_message(msg)
        print(f"Message: {msg}")
        print(f"Category: {category}\n")

if __name__ == "__main__":
    main()