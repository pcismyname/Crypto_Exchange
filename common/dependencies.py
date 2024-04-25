# common/dependencies.py

from fastapi import Header, HTTPException

def get_token_header(x_token: str = Header(...)):
    """Dependency that validates the presence of a token in the header."""
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token
