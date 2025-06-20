import pytesseract
from PIL import Image
import os

# ❌ Comment or remove this line on Streamlit Cloud
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print("🔍 Extracted Text:\n", text)
        return text
    except Exception as e:
        return f"Error reading {image_path}: {e}"
