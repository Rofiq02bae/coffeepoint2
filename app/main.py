from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "Hello from Coffeepoint + Supabase"}

@app.post("/user/{name}")
def create_user(name: str):
    data = {"name": name, "points": 0}
    res = supabase.table("users").insert(data).execute()
    return res.data

@app.get("/users")
def get_users():
    res = supabase.table("users").select("*").execute()
    return res.data
