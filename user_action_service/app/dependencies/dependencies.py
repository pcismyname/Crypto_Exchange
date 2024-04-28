# dependencies.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from app.models.model import User

SECRET_KEY = "8a9b1f3cfb45729b1042b2ecb3ba1d6e429c1245ce64f20eff86b0975c6b77bb"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8077/api/v1/login")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://auth:8000/api/v1/login")


def get_user_from_token(token: str, db: Session) -> User:
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: int = payload.get("sub")  # 'sub' is typically used to store the user identifier
        if not email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Retrieve the user from the database
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


# Replace with your actual database URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@postgres/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo = True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Use this contextmanager to wrap database operations in a session, ensuring they commit or rollback
@contextmanager
def get_db_context():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
