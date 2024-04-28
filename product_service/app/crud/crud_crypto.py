# product_service/app/crud/crud_cryptocurrency.py

from sqlalchemy.orm import Session
from app.models.model import Cryptocurrency, Inventory
from app.schemas.schemas import CryptocurrencyCreate, CryptocurrencyUpdate

def create_cryptocurrency(db: Session, cryptocurrency_data: CryptocurrencyCreate) -> Cryptocurrency:
    db_cryptocurrency = Cryptocurrency(
        name=cryptocurrency_data.name,
        symbol=cryptocurrency_data.symbol
    )
    db.add(db_cryptocurrency)
    db.commit()
    db.refresh(db_cryptocurrency)

    db_inventory = Inventory(
        crypto_id=db_cryptocurrency.crypto_id,
        total_amount=0.0,  # Default value
        reserved_amount=0.0  # Default value
    )
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)

    return db_cryptocurrency

def get_cryptocurrency(db: Session, crypto_id: int) -> Cryptocurrency:
    return db.query(Cryptocurrency).filter(Cryptocurrency.crypto_id == crypto_id).first()

def get_all_cryptocurrencies(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(Cryptocurrency).offset(skip).limit(limit).all()

def update_cryptocurrency_db(db: Session, crypto_id: int, cryptocurrency_data: CryptocurrencyUpdate) -> Cryptocurrency:
    db_cryptocurrency = db.query(Cryptocurrency).filter(Cryptocurrency.crypto_id == crypto_id).first()
    if db_cryptocurrency:
        db_cryptocurrency.name = cryptocurrency_data.name
        db_cryptocurrency.symbol = cryptocurrency_data.symbol
        db.commit()
        db.refresh(db_cryptocurrency)
    return db_cryptocurrency

def delete_cryptocurrency_db(db: Session, crypto_id: int):
    db_cryptocurrency = db.query(Cryptocurrency).filter(Cryptocurrency.crypto_id == crypto_id).first()
    if db_cryptocurrency:
        db.delete(db_cryptocurrency)
        db.commit()
        return True
    return False
