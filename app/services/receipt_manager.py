def generate_receipt(tx_data: dict, qr_url: str) -> str:
    return f"""
    ===== COFFEEPOINT RECEIPT =====
    User: {tx_data['user_id']}
    Total: Rp {tx_data['total_price']}
    Time: {tx_data['timestamp']}
    QR Code: {qr_url}
    ================================
    """
