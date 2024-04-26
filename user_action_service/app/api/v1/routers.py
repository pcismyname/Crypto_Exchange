from fastapi import APIRouter
from app.api.v1.endpoints import wallet, transaction

api_router = APIRouter()
api_router.include_router(wallet.router, prefix="/wallets", tags=["Wallets"])
api_router.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])
