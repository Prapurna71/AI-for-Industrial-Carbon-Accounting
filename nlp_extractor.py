import re

def extract_energy_data(text):
    extracted = {
        'electricity_kwh': 0.0,
        'diesel_litres': 0.0,
        'petrol_litres': 0.0,
        'natural_gas_m3': 0.0
    }

    # 🧹 Clean and normalize text
    text = text.lower()
    text = text.replace(',', '')
    text = text.replace('ltr', 'litres').replace('lt', 'litres').replace('l ', 'litres ')
    text = text.replace(':', ' ').replace('  ', ' ')

    # ✅ Electricity
    kwh_matches = re.findall(r'(\d+\.?\d*)\s*kwh', text)
    if kwh_matches:
        extracted['electricity_kwh'] = sum(float(k) for k in kwh_matches)

    # ✅ Diesel (not found in this example, but still included)
    diesel_matches = re.findall(r'(\d+\.?\d*)\s*litres.*?(diesel|high speed)?', text)
    if diesel_matches:
        extracted['diesel_litres'] = sum(float(m[0]) for m in diesel_matches)

    # ✅ Petrol
    petrol_matches = re.findall(r'(\d+\.?\d*)\s*litres.*?(petrol)?', text)
    if petrol_matches:
        extracted['petrol_litres'] = sum(float(m[0]) for m in petrol_matches)

    # ✅ Natural Gas
    gas_matches = re.findall(r'(\d+\.?\d*)\s*m3.*?(natural gas)?', text)
    if gas_matches:
        extracted['natural_gas_m3'] = sum(float(m[0]) for m in gas_matches)

    return extracted


# 🧪 Debug mode
if __name__ == "__main__":
    with open("extracted_text/Screenshot 2025-06-20 225423.png.txt", "r", encoding="utf-8") as f:
        invoice_text = f.read()
    result = extract_energy_data(invoice_text)
    print("\n✅ Extracted Emission Data:")
    for k, v in result.items():
        print(f"{k}: {v}")
