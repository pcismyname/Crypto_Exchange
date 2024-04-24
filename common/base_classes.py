# common/base_classes.py

from pydantic import BaseModel
from typing import Optional

class CustomBaseModel(BaseModel):
    """
    Custom base class for Pydantic models that adds common settings.
    """
    class Config:
        orm_mode = True
        anystr_strip_whitespace = True
