import re

def extract_energy_data(text):
    extracted = {
        'electricity_kwh': 0,
        'diesel_litres': 0,
        'petrol_litres': 0,
        'natural_gas_m3': 0
    }

    # Remove commas
    text = text.replace(',', '')

    # Electricity
    kwh_matches = re.findall(r'(\d+\.?\d*)\s?kWh', text, re.IGNORECASE)
    if kwh_matches:
        extracted['electricity_kwh'] = sum(float(k) for k in kwh_matches)

    # Diesel — match lines with diesel + litre, regardless of order
    diesel_matches = re.findall(r'(?:diesel[^\n]*?(\d+\.?\d*)\s?(litres|liter|l))|(?:(\d+\.?\d*)\s?(litres|liter|l)[^\n]*?diesel)', text, re.IGNORECASE)
    for match in diesel_matches:
        # match[0] OR match[2] contains the number depending on match side
        val = match[0] or match[2]
        if val:
            extracted['diesel_litres'] += float(val)

    # Petrol — same pattern for symmetry
    petrol_matches = re.findall(r'(?:petrol[^\n]*?(\d+\.?\d*)\s?(litres|liter|l))|(?:(\d+\.?\d*)\s?(litres|liter|l)[^\n]*?petrol)', text, re.IGNORECASE)
    for match in petrol_matches:
        val = match[0] or match[2]
        if val:
            extracted['petrol_litres'] += float(val)

    # Natural gas
    gas_matches = re.findall(r'(\d+\.?\d*)\s?(m3|m³)[^\n]*natural gas', text, re.IGNORECASE)
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
