# user_action_service/app/crud/wallet_crud.py

from sqlalchemy.orm import Session
from app.models.model import Wallet, Cryptocurrency
from app.schemas.schemas import WalletCreate, WalletUpdate

def get_wallet(db: Session, wallet_id: int):
    return db.query(Wallet).filter(Wallet.wallet_id == wallet_id).first()

def get_wallets_by_user(db: Session, user_id: int):
    return db.query(Wallet).filter(Wallet.user_id == user_id).all()

def get_wallet_by_user_id_and_currency_id(db: Session, user_id: int, currency_id: int) -> Wallet:
  return db.query(Wallet).filter(Wallet.user_id == user_id, Wallet.currency_id == currency_id).first()


def create_wallet(db: Session, wallet_data: WalletCreate):
    db_wallet = Wallet(**wallet_data.dict())
    db.add(db_wallet)
    db.commit()
    db.refresh(db_wallet)
    return db_wallet

def update_wallet_balance(db: Session, wallet_id: int, amount: float):
    db_wallet = get_wallet(db, wallet_id)
    if db_wallet:
        db_wallet.balance += amount  # Adjust balance based on transaction type in calling function
        db.commit()
        db.refresh(db_wallet)
    return db_wallet

def delete_wallet(db: Session, wallet_id: int):
    db_wallet = get_wallet(db, wallet_id)
    if db_wallet:
        db.delete(db_wallet)
        db.commit()
        return True
    return False
