# user_action_service/app/crud/transaction_crud.py

from sqlalchemy.orm import Session
from app.models.model import Transaction
from app.schemas.schemas import TransactionCreate

def create_transaction(db: Session, transaction_data: TransactionCreate):
    db_transaction = Transaction(**transaction_data.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions_by_wallet(db: Session, wallet_id: int):
    return db.query(Transaction).filter(Transaction.wallet_id == wallet_id).all()

def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
