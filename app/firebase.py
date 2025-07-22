import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64

cred_base64 = os.getenv("FIREBASE_CREDENTIAL")

if cred_base64:
    with open("coffeepoint.json", "wb") as f:
        f.write(base64.b64decode(cred_base64))

if not firebase_admin._apps:
    cred = credentials.Certificate("coffeepoint2.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()





