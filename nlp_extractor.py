import re

def extract_energy_data(text):
    data = {}

    # Normalize text
    text = text.replace(',', '')         # Remove commas from numbers
    text = text.replace(':', ' ')        # Replace colons (OCR sometimes adds them)
    text = text.lower()                  # Case-insensitive match
    text = text.replace('ltr', 'litres')
    text = text.replace('lt', 'litres')  # Normalize 'lt' to 'litres'

    # --- Extract Electricity ---
    electricity_match = re.search(r'electricity.*?(\d+\.?\d*)\s*kwh', text)
    if electricity_match:
        data['electricity_kwh'] = float(electricity_match.group(1))
    else:
        data['electricity_kwh'] = 0.0

    # --- Extract Diesel ---
    diesel_match = re.search(r'diesel.*?(\d+\.?\d*)\s*litres', text)
    if diesel_match:
        data['diesel_litres'] = float(diesel_match.group(1))
    else:
        data['diesel_litres'] = 0.0

    # --- Extract Petrol ---
    petrol_match = re.search(r'petrol.*?(\d+\.?\d*)\s*litres', text)
    if petrol_match:
        data['petrol_litres'] = float(petrol_match.group(1))
    else:
        data['petrol_litres'] = 0.0

    # --- Extract Natural Gas ---
    gas_match = re.search(r'natural\s*gas.*?(\d+\.?\d*)\s*m3', text)
    if gas_match:
        data['natural_gas_m3'] = float(gas_match.group(1))
    else:
        data['natural_gas_m3'] = 0.0

    print("✅ Extracted Emission Data:")
    for k, v in data.items():
        print(f"{k}: {v}")

    return data

# Optional test
if __name__ == "__main__":
    with open("extracted_text/invoice1.jpg.txt", "r", encoding="utf-8") as f:
        invoice_text = f.read()
        extract_energy_data(invoice_text)
