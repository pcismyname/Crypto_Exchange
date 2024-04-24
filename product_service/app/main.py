from fastapi import FastAPI
from app.api.v1.endpoints import product_router


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World from Product Service"}

app.include_router(product_router.router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)