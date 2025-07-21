from firebase_admin import firestore
from datetime import datetime
from typing import Dict, Any

class Transaction:
    def __init__(self, tx_id: str, user_id: str, total_amount: float, timestamp: datetime):
        self.tx_id = tx_id
        self.user_id = user_id
        self.total_amount = total_amount
        self.timestamp = timestamp
        self._db = firestore.client()
    
    async def save(self) -> Dict[str, Any]:
        tx_data = {
            'tx_id': self.tx_id,
            'user_id': self.user_id,
            'total_amount': self.total_amount,
            'timestamp': self.timestamp
        }
        
        self._db.collection('transactions').document(self.tx_id).set(tx_data)
        return tx_data