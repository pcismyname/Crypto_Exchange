from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import wallet_crud
from app.schemas.schemas import WalletOut, WalletCreate
from app.dependencies.dependencies import get_db, get_user_from_token, oauth2_scheme
from typing import List
router = APIRouter()


@router.get("/", response_model=List[WalletOut])
def get_all_wallet_ids(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = get_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or user not found")

    wallet_ids = wallet_crud.get_wallets_by_user(db, user.user_id)
    return wallet_ids


@router.get("/{wallet_id}", response_model=WalletOut)
def read_wallet(wallet_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = get_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or user not found")
    
    wallet = wallet_crud.get_wallet(db, wallet_id=wallet_id)
    if not wallet or wallet.user_id != user.user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wallet not found")
    return wallet

@router.post("/", response_model=WalletOut)
def create_wallet(wallet_data: WalletCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = get_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or user not found")
    
    # Ensure wallet_data includes the user_id from the authenticated user
    wallet_data.user_id = user.user_id
    wallet = wallet_crud.create_wallet(db, wallet_data=wallet_data)
    return wallet
