# user_service/app/models/user_model.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from database import Base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    wallets = relationship("Wallet", back_populates="owner")

class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    crypto_id = Column(Integer, ForeignKey('cryptocurrencies.crypto_id'))
    amount = Column(Float, default=0)  # Stores the amount of cryptocurrency
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship to user and cryptocurrency
    user = relationship("User", back_populates="wallets")
    cryptocurrency = relationship("Cryptocurrency", back_populates="wallets")

