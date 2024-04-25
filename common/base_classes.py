# common/base_classes.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CustomBaseModel(BaseModel):
    """
    Custom base class for Pydantic models that adds common settings.
    """
    class Config:
        orm_mode = True
        anystr_strip_whitespace = True

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    username: str
