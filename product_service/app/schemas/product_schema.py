# product_service/app/schemas/product_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
