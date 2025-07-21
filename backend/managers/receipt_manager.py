from datetime import datetime

class ReceiptManager:
    def generate(self, customer_name: str, tx_id: str, total: float, 
                timestamp: datetime, points: int) -> str:
        receipt = f"""
        === COFFEEPOINT ===
        
        Transaction ID: {tx_id}
        Customer: {customer_name}
        Date: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        
        Total: Rp {total:,.2f}
        
        Current Points: {points}
        
        Thank you for visiting!
        ===================
        """
        return receipt.strip()