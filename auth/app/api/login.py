# user_service/app/api/v1/endpoints/login.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import verify_password, create_access_token
from app.crud.crud import get_user_by_email_in_db
from app.dependencies.dependencies import get_db, get_current_user
from datetime import timedelta
from app.models.user_model import User


ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

@router.post("/")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = get_user_by_email_in_db(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/send-token")
def send_token(token: str):
    # Here you can perform any additional logic, such as sending the token via email or any other method
    return {"token": token}

# @router.get("/user/me")
# async def get_current_authenticated_user(current_user: User = Depends(get_current_user)):
#     return current_user

