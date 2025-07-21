import qrcode
import base64
from io import BytesIO

class QRCodeManager:
    def generate(self, tx_id: str) -> str:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(tx_id)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to base64 for frontend
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()