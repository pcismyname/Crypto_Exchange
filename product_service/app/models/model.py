from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


print('creating base')
Base = declarative_base()

class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrencies'

    crypto_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    symbol = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to Inventory
    inventory = relationship("Inventory", back_populates="cryptocurrency", uselist=False)

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, index=True)
    crypto_id = Column(Integer, ForeignKey('cryptocurrencies.crypto_id'), unique=True)
    total_amount = Column(Float, nullable=False)
    reserved_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to Cryptocurrency
    cryptocurrency = relationship("Cryptocurrency", back_populates="inventory")

