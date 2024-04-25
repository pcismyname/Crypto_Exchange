from fastapi import APIRouter
from ..api import  login, register

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(register.router, prefix="/register", tags=["register"])
