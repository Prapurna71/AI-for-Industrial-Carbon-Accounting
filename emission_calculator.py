import pandas as pd
from nlp_extractor import extract_energy_data

def normalize_unit(unit):
    """Convert common unit variants to standard CSV format"""
    unit = unit.lower().strip()
    if unit in ['lt', 'ltr', 'l']:
        return 'litres'
    if unit in ['kwh', 'kilowatt-hour', 'kilowatthour']:
        return 'kWh'
    if unit in ['m3', 'cubic meter', 'cubicmetre']:
        return 'm3'
    return unit

def calculate_emissions(text_file, factors_csv='emission_data/emission_factors.csv'):
    # Load emission factors
    df = pd.read_csv(factors_csv)
    factors = {row['source']: row['co2_factor'] for _, row in df.iterrows()}
    units = {row['source']: row['unit'] for _, row in df.iterrows()}

    # Read invoice text
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Extract data from invoice
    extracted = extract_energy_data(text)

    # Calculate CO2 emissions
    results = {}
    total_emissions = 0.0

    for source in extracted:
        amount = extracted[source]
        normalized_source = source.replace('_kwh', '').replace('_litres', '').replace('_m3', '')
        normalized_source = normalized_source.strip()

        co2_factor = factors.get(normalized_source, 0)
        unit = units.get(normalized_source, '')

        emissions = amount * co2_factor
        results[source] = {
            'amount': amount,
            'unit': unit,
            'co2_factor': co2_factor,
            'emissions_kg': round(emissions, 2)
        }

        total_emissions += emissions

    return results, round(total_emissions, 2)

if __name__ == "__main__":
    results, total = calculate_emissions('extracted_text/invoice1.jpg.txt')

    print("\n🌍 CO₂ Emission Summary:")
    for k, v in results.items():
        print(f"{k} → {v['amount']} {v['unit']} × {v['co2_factor']} = {v['emissions_kg']} kg CO₂")
    print(f"\n🟢 Total Emissions: {total} kg CO₂")
