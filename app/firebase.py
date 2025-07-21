import firebase_admin
from firebase_admin import credentials, firestore
import os

if not firebase_admin._apps:
    cred = credentials.Certificate("coffeepoint2.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
