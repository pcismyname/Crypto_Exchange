# product_service/app/crud/product_crud.py
from sqlalchemy.orm import Session
from ..models.product_model import Product
from ..schemas.product_schema import ProductCreate

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product(db, product_id=product_id)
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id=product_id)
    db.delete(db_product)
    db.commit()
    return db_product
