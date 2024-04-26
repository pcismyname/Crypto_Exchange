# product_service/app/api/v1/router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud.crud_crypto import (create_cryptocurrency, get_cryptocurrency,
                                 update_cryptocurrency, delete_cryptocurrency,
                                  get_all_cryptocurrencies)
from app.schemas.schemas import (CryptocurrencyCreate, CryptocurrencyInDBBase,
                         CryptocurrencyUpdate)
from app.dependencies.dependencies import get_db

router = APIRouter()

# Cryptocurrency Endpoints
@router.post("/cryptocurrencies/", response_model=CryptocurrencyInDBBase)
def create_new_cryptocurrency(cryptocurrency: CryptocurrencyCreate, db: Session = Depends(get_db)):
    return create_cryptocurrency(db=db, cryptocurrency_data=cryptocurrency)

@router.get("/cryptocurrencies/", response_model=List[CryptocurrencyInDBBase])
def read_cryptocurrencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_cryptocurrencies(db=db, skip=skip, limit=limit)

@router.get("/cryptocurrencies/{crypto_id}", response_model=CryptocurrencyInDBBase)
def read_cryptocurrency(crypto_id: int, db: Session = Depends(get_db)):
    db_crypto = get_cryptocurrency(db=db, crypto_id=crypto_id)
    if db_crypto is None:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")
    return db_crypto

@router.put("/cryptocurrencies/{crypto_id}", response_model=CryptocurrencyInDBBase)
def update_cryptocurrency(crypto_id: int, cryptocurrency: CryptocurrencyUpdate, db: Session = Depends(get_db)):
    updated_crypto = update_cryptocurrency(db=db, crypto_id=crypto_id, cryptocurrency_data=cryptocurrency)
    if not updated_crypto:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")
    return updated_crypto

@router.delete("/cryptocurrencies/{crypto_id}", status_code=204)
def delete_a_cryptocurrency(crypto_id: int, db: Session = Depends(get_db)):
    if not delete_cryptocurrency(db=db, crypto_id=crypto_id):
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")

# Inventory Endpoints (similar structure)
# Define routes for create_inventory, get_inventory, update_inventory, delete_inventory

