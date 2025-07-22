import firebase_admin
from firebase_admin import credentials
import base64
import json
import os

cred_json = base64.b64decode(os.getenv("FIREBASE_CREDENTIALS")).decode("utf-8")
cred_dict = json.loads(cred_json)
cred = credentials.Certificate(cred_dict)

firebase_admin.initialize_app(cred)
