from fastapi import FastAPI, HTTPException
from models.user import User
from models.transaction import Transaction
from managers.qr_manager import QRCodeManager
from managers.receipt_manager import ReceiptManager
from firebase_admin import initialize_app, credentials
import firebase_admin
import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = FastAPI(title="Coffeepoint API")

class TransactionRequest(BaseModel):
    user_id: str
    total_amount: float
    customer_name: str

@app.post("/transaction")
async def create_transaction(req: TransactionRequest):
    try:
        # Create transaction object
        transaction = Transaction(
            tx_id=str(uuid.uuid4()),
            user_id=req.user_id,
            total_amount=req.total_amount,
            timestamp=datetime.now()
        )
        
        # Save to Firebase
        saved_tx = await transaction.save()
        
        # Calculate loyalty points
        user = await User.get_by_id(req.user_id)
        user.add_points(1)  # 1 point per transaction
        
        # Check if user gets voucher
        voucher = None
        if user.points % 5 == 0:
            voucher = "DISCOUNT10"  # Simple voucher implementation
            
        # Generate QR Code
        qr_manager = QRCodeManager()
        qr_code = qr_manager.generate(transaction.tx_id)
        
        # Generate receipt
        receipt_manager = ReceiptManager()
        receipt = receipt_manager.generate(
            customer_name=req.customer_name,
            tx_id=transaction.tx_id,
            total=req.total_amount,
            timestamp=transaction.timestamp,
            points=user.points
        )
        
        return {
            "success": True,
            "data": {
                "transaction": saved_tx,
                "receipt": receipt,
                "qr_code": qr_code,
                "voucher": voucher,
                "points": user.points
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))