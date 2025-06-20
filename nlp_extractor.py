import re

def extract_energy_data(text):
    extracted = {
        'electricity_kwh': 0,
        'diesel_litres': 0,
        'petrol_litres': 0,
        'natural_gas_m3': 0
    }

    # Remove commas (e.g., 129,491 → 129491)
    text = text.replace(',', '')

    # Extract electricity usage in kWh
    kwh_matches = re.findall(r'(\d+\.?\d*)\s?kWh', text, re.IGNORECASE)
    if kwh_matches:
        extracted['electricity_kwh'] = sum(float(k) for k in kwh_matches)

    # Diesel in litres
    diesel_matches = re.findall(r'(\d+\.?\d*)\s?(litres|liter|l)\s?(diesel)?', text, re.IGNORECASE)
    if diesel_matches:
        extracted['diesel_litres'] = sum(float(m[0]) for m in diesel_matches)

    # Petrol in litres
    petrol_matches = re.findall(r'(\d+\.?\d*)\s?(litres|liter|l)\s?(petrol)?', text, re.IGNORECASE)
    if petrol_matches:
        extracted['petrol_litres'] = sum(float(m[0]) for m in petrol_matches)

    # Natural gas in m3
    gas_matches = re.findall(r'(\d+\.?\d*)\s?(m3|m³)\s?(natural gas)?', text, re.IGNORECASE)
    if gas_matches:
        extracted['natural_gas_m3'] = sum(float(m[0]) for m in gas_matches)

    return extracted

if __name__ == "__main__":
    with open("extracted_text/invoice1.jpg.txt", "r", encoding='utf-8') as f:
        invoice_text = f.read()

    result = extract_energy_data(invoice_text)
    print("\n✅ Extracted Emission Data:")
    for k, v in result.items():
        print(f"{k}: {v}")
