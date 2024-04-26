from fastapi import APIRouter
from app.api.v1.endpoints import crypto, inventory

api_router = APIRouter()
api_router.include_router(crypto.router, tags=['crypto'])
api_router.include_router(inventory.router, tags=['inventory'])

