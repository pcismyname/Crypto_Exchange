from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import verify_password, create_access_token
from app.crud.crud import get_user_by_email_in_db, create_user_in_db
from app.dependencies.dependencies import get_db
from datetime import timedelta
from app.models.user_model import User
from requests import post

router = APIRouter()


@router.post("/")
def register_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    # Check if the user already exists
    existing_user = get_user_by_email_in_db(db, form_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    
    # Make a POST request to the other API to register the user
    user_data = {"email": form_data.username, "password": form_data.password}
    response = post("http://user_service:8000/api/v1/users", json=user_data)
    
    # Check if the registration was successful
    if response.status_code == status.HTTP_201_CREATED:
        return {"message": "User registered successfully"}
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to register user",
        )
