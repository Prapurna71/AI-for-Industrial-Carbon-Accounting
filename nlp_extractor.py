import re

def extract_energy_data(text):
    extracted = {
        'electricity_kwh': 0.0,
        'diesel_litres': 0.0,
        'petrol_litres': 0.0,
        'natural_gas_m3': 0.0
    }

    # Normalize text
    text = text.replace(',', '').lower()
    text = text.replace('ltr', 'litres').replace('lt', 'litres').replace(':', ' ')

    # Match electricity usage
    kwh_matches = re.findall(r'(\d+\.?\d*)\s*kwh', text, re.IGNORECASE)
    if kwh_matches:
        extracted['electricity_kwh'] = sum(float(k) for k in kwh_matches)

    # Match diesel (litres)
    diesel_matches = re.findall(r'(\d+\.?\d*)\s*litres.*?(diesel)?', text, re.IGNORECASE)
    if diesel_matches:
        extracted['diesel_litres'] = sum(float(m[0]) for m in diesel_matches)

    # Match petrol
    petrol_matches = re.findall(r'(\d+\.?\d*)\s*litres.*?(petrol)?', text, re.IGNORECASE)
    if petrol_matches:
        extracted['petrol_litres'] = sum(float(m[0]) for m in petrol_matches)

    # Match natural gas
    gas_matches = re.findall(r'(\d+\.?\d*)\s*m3.*?(natural gas)?', text, re.IGNORECASE)
    if gas_matches:
        extracted['natural_gas_m3'] = sum(float(m[0]) for m in gas_matches)

    print("\n✅ Extracted Emission Data:")
    for k, v in extracted.items():
        print(f"{k}: {v}")

    return extracted
