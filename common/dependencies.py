<<<<<<< HEAD
# common/dependencies.py

# dependencies.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.core.security import SECRET_KEY, ALGORITHM
from app.crud.crud import get_user_in_db
from app.schemas.user_schema import TokenData


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

async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_in_db(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_token_header(x_token: str = Header(...)):
    """Dependency that validates the presence of a token in the header."""
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token

=======
>>>>>>> parent of dba30bd (generate token)
