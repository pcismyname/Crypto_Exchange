# product_service/app/schemas.py

from pydantic import BaseModel
from datetime import datetime

class CryptocurrencyBase(BaseModel):
    name: str
    symbol: str

class CryptocurrencyCreate(CryptocurrencyBase):
    pass

class CryptocurrencyUpdate(CryptocurrencyBase):
    pass

class CryptocurrencyInDBBase(CryptocurrencyBase):
    crypto_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    crypto_id: int
    total_amount: float
    reserved_amount: float

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(InventoryBase):
    pass

class InventoryInDBBase(InventoryBase):
    created_at: datetime

    class Config:
        orm_mode = True
