from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import transaction_crud, wallet_crud
from app.schemas.schemas import  WalletCreate
from app.schemas.schemas import TransactionCreate, TransactionOut
from app.dependencies.dependencies import get_db, get_user_from_token, oauth2_scheme
import requests  # For making HTTP requests to product_service

router = APIRouter()

router = APIRouter()

@router.post("/buy", response_model=TransactionOut)
def buy_crypto(
    transaction_data: TransactionCreate, 
    db: Session = Depends(get_db), 
    token: str = Depends(oauth2_scheme)
):
    # Authenticate and get the user
    user = get_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or user not found")

    # Check if a wallet with the specified currency_id exists for the user
    wallet = wallet_crud.get_wallet_by_user_id_and_currency_id(db, user_id=user.user_id, currency_id=transaction_data.currency_id)
    
    # If wallet does not exist, create it with a zero balance
    if not wallet:
        wallet_data = WalletCreate(user_id=user.user_id, currency_id=transaction_data.currency_id, balance=0)
        wallet = wallet_crud.create_wallet(db, wallet_data=wallet_data)
    
    # Check if the user has enough balance in the wallet
    # if wallet.balance < transaction_data.amount:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient funds")

    # /api/v1/inventory/1/decrease
    # /api/v1/inventory/1/decrease?amount=1
    # Check and update inventory via product_service
    # print(transaction_data.currency_id, transaction_data.amount)
    # response = requests.post(f"http://product_service:8000/api/v1/inventory/{transaction_data.currency_id}/decrease", json={"amount": transaction_data.amount})
    # print(requests.post(f"http://product_service:8000/api/v1/inventory/{transaction_data.currency_id}/decrease", json={"amount": transaction_data.amount}).url)
    url = f"http://product_service:8000/api/v1/inventory/{transaction_data.currency_id}/decrease/"  # Assuming URL structure
    params = {"amount": transaction_data.amount}  # Define query parameters
    response = requests.post(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="Failed to update inventory")

    # Proceed with the transaction
    transaction = transaction_crud.create_transaction(db, transaction_data=transaction_data)
    
    # If transaction is successful, deduct amount from wallet balance
    if transaction:
        wallet.balance += transaction_data.amount
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction failed")

    return transaction
