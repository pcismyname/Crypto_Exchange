from fastapi import FastAPI
from app.api.v1.routers import api_router
from app.models.model import Base  
from app.dependencies.dependencies import engine
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("init lifespan")
    Base.metadata.create_all(bind=engine)  # Create database tables
    print("Database tables created!")

app = FastAPI(lifespan=lifespan)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# async def on_startup():
#     Base.metadata.create_all(bind=engine)  # Create database tables
#     print("Database tables created!")



# Include routers
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "Welcome to the user action service API"}

# Base.metadata.create_all(bind=engine)  # Create database tables
print("Database tables created!")


