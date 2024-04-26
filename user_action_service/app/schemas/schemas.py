# user_action_service/app/schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Wallet Schemas
class WalletBase(BaseModel):
    user_id: int
    currency_id: int
    balance: float = 0.0

class WalletCreate(WalletBase):
    pass

class WalletUpdate(BaseModel):
    balance: Optional[float] = None

class WalletOut(WalletBase):
    wallet_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Transaction Schemas
class TransactionBase(BaseModel):
    wallet_id: int
    currency_id: int
    amount: float
    type: str  # 'buy' or 'sell'
    price_per_unit: float

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    transaction_id: int
    transaction_date: datetime

    class Config:
        orm_mode = True
