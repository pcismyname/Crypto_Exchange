from fastapi import FastAPI
from app.api.routers import api_router
from .db import SQLALCHEMY_DATABASE_URL
from sqlalchemy import create_engine
from contextlib import asynccontextmanager
from app.models.user_model import Base  # Import Base from your model file
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)  # Create database tables
    print("Database tables created!")
    try:
        yield
    finally:
        engine.dispose()  # Close the database connection
        print("Database connection closed!")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World from Authen service"}

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)