# user_service/app/api/v1/endpoints/protected_endpoint.py

from fastapi import Depends, HTTPException
from app.dependencies import get_current_user

@router.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
