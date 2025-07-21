# from fastapi import FastAPI
# from routes import transaction

# app = FastAPI(title="Coffeepoint API")

# app.include_router(transaction.router, prefix="/transaction", tags=["Transaction"])

# @app.get("/")
# def read_root():
#     return {"message": "Coffeepoint Backend is running!"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Coffeepoint API!"}
