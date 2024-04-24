# crud.py in user_service/app/crud
import bcrypt
from sqlalchemy.orm import Session
from app.models import user_model
from app.schemas.user_schema import UserCreate, UserOut, UserUpdate

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def get_user_in_db(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_user_by_email_in_db(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def get_users_in_db(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

def create_user_in_db(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)  # Hashing the password
    db_user = user_model.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_in_db(db: Session, user_id: int, update_data: UserUpdate):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not db_user:
        return None
    if update_data.password:
        update_data.password = hash_password(update_data.password)  # Re-hash updated password
    for var, value in vars(update_data).items():
        setattr(db_user, var, value) if value else None
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_in_db(db: Session, user_id: int):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False
