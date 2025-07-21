from fastapi import APIRouter
from models.transaction import Transaction
from firebase import db
from services.receipt_manager import generate_receipt
from services.qrcode_manager import generate_qr

router = APIRouter()

@router.post("/")
def create_transaction(tx: Transaction):
    doc_ref = db.collection("transactions").document()
    tx_data = tx.dict()
    tx_data["id"] = doc_ref.id
    doc_ref.set(tx_data)

    qr = generate_qr(doc_ref.id)
    receipt = generate_receipt(tx_data, qr)

    return {
        "message": "Transaction created!",
        "transaction_id": doc_ref.id,
        "receipt": receipt
    }
