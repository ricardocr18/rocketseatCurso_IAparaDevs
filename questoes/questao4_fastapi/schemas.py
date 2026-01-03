from pydantic import BaseModel
from datetime import date

class ItemBase(BaseModel):
    nome: str
    valor: float
    data: date

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: str

    class Config:
        orm_mode = True