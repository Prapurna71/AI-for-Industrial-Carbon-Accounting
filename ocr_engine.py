from PIL import Image
import pytesseract
import os

# ✅ Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print("📄 Extracted OCR Text:\n", text)  # Optional: For debug
        return text
    except Exception as e:
        return f"Error reading {image_path}: {e}"

def process_invoices(input_folder='invoices', output_folder='extracted_text'):
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff')):
            img_path = os.path.join(input_folder, file_name)
            print(f"🔍 Processing: {img_path}")
            text = extract_text_from_image(img_path)
            output_file = os.path.join(output_folder, file_name + '.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"✅ Text saved to {output_file}")

# 🧪 Debug/Test
if __name__ == '__main__':
    process_invoices()
