# user_service/app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.crud.crud import (
    get_user_by_email_in_db,
    create_user_in_db,
    get_users_in_db,
    get_user_in_db,
    update_user_in_db,
    delete_user_in_db,
)
from app.dependencies.dependencies import get_db
from app.schemas.user_schema import UserCreate, UserOut, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email_in_db(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user_in_db(db=db, user=user)

@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users_in_db(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_in_db(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user_in_db(db, user_id=user_id, update_data=user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not delete_user_in_db(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True}
