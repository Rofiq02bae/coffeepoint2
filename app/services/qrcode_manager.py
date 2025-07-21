import qrcode
import base64
from io import BytesIO

def generate_qr(data: str) -> str:
    img = qrcode.make(data)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode()
