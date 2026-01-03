"""
Questão 4: Endpoint FastAPI com validação de Item
Desafio de Prompt Engineering - Nível 6

Requisitos:
1. Validar Item (nome ≤25 chars, valor float, data ≤hoje)
2. Retornar Item com UUID gerado automaticamente

Executar:
    uvicorn main:app --reload
    
    OU
    
    python main.py

Acessar documentação:
    http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from uuid import uuid4

# Importar modelos da pasta questoes/questao4_fastapi
from questoes.questao4_fastapi.models import Item, ItemResponse

# Criar aplicação FastAPI
app = FastAPI(
    title="Prompt Engineering Challenge - Questão 4",
    description="Endpoint de validação e processamento de Item com UUID",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================== ENDPOINTS ====================

@app.get(
    "/",
    tags=["Root"],
    summary="Informações da API"
)
async def root():
    """
    Endpoint raiz com informações da API.
    """
    return {
        "message": "API de Validação de Item - Prompt Engineering Challenge",
        "version": "1.0.0",
        "questao": "Questão 4",
        "desafio": "Prompt Engineering - Nível 6",
        "endpoints": {
            "POST /item": "Criar e validar um item (retorna com UUID)",
            "GET /docs": "Documentação interativa (Swagger UI)",
            "GET /redoc": "Documentação alternativa (ReDoc)",
            "GET /health": "Health check da aplicação"
        },
        "especificacoes": {
            "nome": "string (máximo 25 caracteres)",
            "valor": "float",
            "data": "date (não pode ser futura)"
        }
    }


@app.post(
    "/item",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Item"],
    summary="Criar e validar Item",
    description="""
    ## Cria um novo item com validações automáticas:
    
    ### Validações:
    - **nome**: Máximo 25 caracteres, não pode ser vazio
    - **valor**: Deve ser um número float (decimal)
    - **data**: Não pode ser superior à data atual
    
    ### Retorno:
    - Item validado com campo **uuid** gerado automaticamente
    
    ### Exemplo de Request:
    ```json
    {
      "nome": "Mouse Gamer",
      "valor": 150.00,
      "data": "2025-01-02"
    }
    ```
    
    ### Exemplo de Response:
    ```json
    {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "nome": "Mouse Gamer",
      "valor": 150.00,
      "data": "2025-01-02"
    }
    ```
    """
)
async def criar_item(item: Item) -> ItemResponse:
    """
    Valida e processa a entrada de um objeto Item.
    
    **Requisito da Questão 4:**
    - Valida os valores recebidos (nome, valor, data)
    - Retorna o Item com campo UUID gerado dinamicamente
    
    Args:
        item: Objeto Item a ser validado
        
    Returns:
        ItemResponse com UUID único gerado
        
    Raises:
        HTTPException: 422 se validação falhar
    """
    try:
        # Gerar UUID único dinamicamente
        item_uuid = uuid4()
        
        # Criar resposta com UUID
        resposta = ItemResponse(
            uuid=item_uuid,
            nome=item.nome,
            valor=item.valor,
            data=item.data
        )
        
        return resposta
    
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(ve)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Erro ao processar item: {str(e)}"
        )


@app.get(
    "/health",
    tags=["Health"],
    summary="Health Check"
)
async def health_check():
    """
    Endpoint de health check para verificar se a API está funcionando.
    """
    return {
        "status": "healthy",
        "timestamp": date.today().isoformat(),
        "service": "Item Validation API",
        "questao": "Questão 4 - Prompt Engineering"
    }


# ==================== EXCEPTION HANDLERS ====================

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    """
    Handler customizado para ValueError (erros de validação).
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": str(exc),
            "type": "validation_error"
        }
    )


# ==================== MAIN ====================

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 80)
    print("🚀 INICIANDO APLICAÇÃO FASTAPI - QUESTÃO 4".center(80))
    print("=" * 80)
    print("\n📋 Informações:")
    print(f"   • Projeto: Desafio de Prompt Engineering - Nível 6")
    print(f"   • Aplicação: Item Validation API")
    print(f"   • Host: http://0.0.0.0:8000")
    print(f"   • Swagger UI: http://localhost:8000/docs")
    print(f"   • ReDoc: http://localhost:8000/redoc")
    print("\n✅ Requisitos implementados:")
    print("   1. Validação de Item (nome ≤25 chars, valor float, data ≤hoje)")
    print("   2. Retorno com UUID gerado automaticamente")
    print("\n📂 Estrutura:")
    print("   • main.py: Aplicação FastAPI (raiz do projeto)")
    print("   • questoes/questao4_fastapi/models.py: Modelos Pydantic")
    print("\n⚡ Pressione CTRL+C para parar o servidor\n")
    print("=" * 80 + "\n")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )