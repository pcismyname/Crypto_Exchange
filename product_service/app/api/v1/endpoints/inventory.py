from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.schemas import InventoryCreate, InventoryInDBBase, InventoryUpdate
from app.crud.crud_inventory import create_inventory, get_inventory, update_inventory, delete_inventory
from app.dependencies.dependencies import get_db

router = APIRouter()

# Create Inventory
@router.post("/inventory/", response_model=InventoryInDBBase, status_code=201)
def create_new_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    return create_inventory(db=db, inventory_data=inventory)

# Get Inventory by Crypto ID
@router.get("/inventory/{crypto_id}", response_model=InventoryInDBBase)
def read_inventory(crypto_id: int, db: Session = Depends(get_db)):
    inventory = get_inventory(db=db, crypto_id=crypto_id)
    if inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found for given cryptocurrency")
    return inventory

# Update Inventory
@router.put("/inventory/{crypto_id}", response_model=InventoryInDBBase)
def update_existing_inventory(crypto_id: int, inventory_data: InventoryUpdate, db: Session = Depends(get_db)):
    updated_inventory = update_inventory(db=db, crypto_id=crypto_id, inventory_data=inventory_data)
    if updated_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return updated_inventory

# Delete Inventory
@router.delete("/inventory/{crypto_id}", status_code=204)
def delete_inventory(crypto_id: int, db: Session = Depends(get_db)):
    if not delete_inventory(db=db, crypto_id=crypto_id):
        raise HTTPException(status_code=404, detail="Inventory not found")
