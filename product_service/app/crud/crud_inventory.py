# product_service/app/crud/crud_inventory.py

from sqlalchemy.orm import Session
from app.models.model import Inventory
from app.schemas.schemas import InventoryCreate, InventoryUpdate

def create_inventory(db: Session, inventory_data: InventoryCreate) -> Inventory:
    db_inventory = Inventory(
        crypto_id=inventory_data.crypto_id,
        total_amount=inventory_data.total_amount,
        reserved_amount=inventory_data.reserved_amount
    )
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def get_inventory(db: Session, crypto_id: int) -> Inventory:
    return db.query(Inventory).filter(Inventory.crypto_id == crypto_id).first()

def update_inventory(db: Session, crypto_id: int, inventory_data: InventoryUpdate) -> Inventory:
    db_inventory = db.query(Inventory).filter(Inventory.crypto_id == crypto_id).first()
    if db_inventory:
        db_inventory.total_amount = inventory_data.total_amount
        db_inventory.reserved_amount = inventory_data.reserved_amount
        db.commit()
        db.refresh(db_inventory)
    return db_inventory

def delete_inventory(db: Session, crypto_id: int):
    db_inventory = db.query(Inventory).filter(Inventory.crypto_id == crypto_id).first()
    if db_inventory:
        db.delete(db_inventory)
        db.commit()
        return True
    return False
