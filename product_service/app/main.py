from fastapi import FastAPI
from app.api.v1.routers import api_router
from app.models.model import Base  
from app.dependencies.dependencies import engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("init lifespan")
    Base.metadata.create_all(bind=engine)  # Create database tables
    yield
    print("Database tables created!")

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    Base.metadata.create_all(bind=engine)  # Create database tables
    print("Database tables created!")



# Include routers
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "Welcome to the Product Service API"}

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # Create database tables
    print("Database tables created!")


