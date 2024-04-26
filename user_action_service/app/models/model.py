# user_action_service/app/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Wallet(Base):
    __tablename__ = 'wallets'
    wallet_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    currency_id = Column(Integer, ForeignKey('cryptocurrencies.crypto_id'), nullable=False)
    balance = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="wallets")
    cryptocurrency = relationship("Cryptocurrency", back_populates="wallets")

class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    wallet_id = Column(Integer, ForeignKey('wallets.wallet_id'), nullable=False)
    currency_id = Column(Integer, ForeignKey('cryptocurrencies.crypto_id'), nullable=False)
    type = Column(String, nullable=False)  # 'buy' or 'sell'
    amount = Column(Float, nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    price_per_unit = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    wallet = relationship("Wallet", back_populates="transactions")
    cryptocurrency = relationship("Cryptocurrency", back_populates="transactions")

class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrencies'
    crypto_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    symbol = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    wallets = relationship("Wallet", back_populates="cryptocurrency")
    transactions = relationship("Transaction", back_populates="cryptocurrency")
    inventory = relationship("Inventory", backref="cryptocurrency", cascade="all, delete-orphan")


class Inventory(Base):
    __tablename__ = 'inventory'
    crypto_id = Column(Integer, ForeignKey('cryptocurrencies.crypto_id'), primary_key=True, index=True)
    total_amount = Column(Float, nullable=False)
    reserved_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Admin(Base):
    __tablename__ = 'admins'
    admin_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserAction(Base):
    __tablename__ = 'user_actions'
    action_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    action_type = Column(String, nullable=False)
    action_description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="actions")

# Define relationships
User.wallets = relationship("Wallet", back_populates="user")
User.actions = relationship("UserAction", back_populates="user")
Wallet.transactions = relationship("Transaction", back_populates="wallet")
# Cryptocurrency.wallets = relationship("Wallet", back_populates="cryptocurrency")
# Cryptocurrency.transactions = relationship("Transaction", back_populates="cryptocurrency")

