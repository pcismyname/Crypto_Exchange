from fastapi import FastAPI
from app.api.v1.routers import api_router
from app.models.user_model import Base  # Import Base from your model file
from app.dependencies.dependencies import SQLALCHEMY_DATABASE_URL
from sqlalchemy import create_engine
from contextlib import asynccontextmanager
import uvicorn


app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
    Base.metadata.create_all(bind=engine)  # Create database tables
    print("Database tables created!")

@app.get("/")
def read_root():
    return {"Hello": "World from User Service"}

app.include_router(api_router, prefix="/api/v1")

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base.metadata.create_all(bind=engine)  # Create database tables


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)