"""
Modelo Pydantic para validação do Item.
Questão 4 - Desafio de Prompt Engineering
"""

from pydantic import BaseModel, Field, field_validator
from datetime import date
from uuid import UUID
from typing import Optional


class Item(BaseModel):
    """
    Modelo de Item com validações conforme especificação.
    
    Attributes:
        nome: String com máximo 25 caracteres
        valor: Float (número decimal)
        data: Date que não pode ser superior à data atual
    """
    nome: str = Field(
        ...,
        max_length=25,
        description="Nome do item (máximo 25 caracteres)",
        examples=["Notebook Dell"]
    )
    
    valor: float = Field(
        ...,
        description="Valor do item (float)",
        examples=[2500.50]
    )
    
    data: date = Field(
        ...,
        description="Data do item (não pode ser futura)",
        examples=["2025-01-02"]
    )
    
    @field_validator('data')
    @classmethod
    def validar_data_nao_futura(cls, v: date) -> date:
        """
        Valida se a data não é superior à data atual.
        
        Args:
            v: Data a ser validada
            
        Returns:
            Data validada
            
        Raises:
            ValueError: Se a data for futura
        """
        hoje = date.today()
        if v > hoje:
            raise ValueError(
                f"Data não pode ser superior à data atual. "
                f"Data fornecida: {v}, Data atual: {hoje}"
            )
        return v
    
    @field_validator('nome')
    @classmethod
    def validar_nome_nao_vazio(cls, v: str) -> str:
        """
        Valida se o nome não é vazio após strip.
        
        Args:
            v: Nome a ser validado
            
        Returns:
            Nome validado (sem espaços extras)
            
        Raises:
            ValueError: Se o nome for vazio
        """
        if not v.strip():
            raise ValueError("Nome não pode ser vazio")
        return v.strip()

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Notebook Dell",
                "valor": 2500.50,
                "data": "2025-01-02"
            }
        }


class ItemResponse(BaseModel):
    """
    Modelo de resposta com UUID gerado.
    
    Attributes:
        uuid: Identificador único gerado automaticamente
        nome: Nome do item
        valor: Valor do item
        data: Data do item
    """
    uuid: UUID = Field(
        ...,
        description="Identificador único do item (gerado automaticamente)"
    )
    nome: str = Field(
        ...,
        description="Nome do item"
    )
    valor: float = Field(
        ...,
        description="Valor do item"
    )
    data: date = Field(
        ...,
        description="Data do item"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "uuid": "550e8400-e29b-41d4-a716-446655440000",
                "nome": "Notebook Dell",
                "valor": 2500.50,
                "data": "2025-01-02"
            }
        }