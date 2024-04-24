# product_service/app/models/product_model.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
