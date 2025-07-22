# from fastapi import FastAPI
# from routes import transaction

# app = FastAPI(title="Coffeepoint API")

# app.include_router(transaction.router, prefix="/transaction", tags=["Transaction"])

# @app.get("/")
# def read_root():
#     return {"message": "Coffeepoint Backend is running!"}
# import firebase_admin
# from firebase_admin import credentials, firestore
# import os
# import base64
# from fastapi import FastAPI

# app = FastAPI()

# cred_base64 = os.getenv("FIREBASE_CREDENTIALS")

# if cred_base64:
#     with open("coffeepoint.json", "wb") as f:
#         f.write(base64.b64decode(cred_base64))

# if not firebase_admin._apps:
#     cred = credentials.Certificate("coffeepoint2.json")
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

# @app.get("/")
# def read_root():
#     return {"message": "Hello from Coffeepoint API!"}
import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64
from fastapi import FastAPI

app = FastAPI()

cred_base64 = os.getenv("FIREBASE_CREDENTIAL")

if cred_base64:
    with open("coffeepoint.json", "wb") as f:
        f.write(base64.b64decode(cred_base64))

if not firebase_admin._apps:
    cred = credentials.Certificate("coffeepoint.json")  # ✅ ini diperbaiki
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.get("/")
def read_root():
    return {"message": "Hello from Coffeepoint API!"}
