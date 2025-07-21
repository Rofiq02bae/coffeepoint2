from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    user_id: str
    total_price: float
    timestamp: datetime = datetime.utcnow()
