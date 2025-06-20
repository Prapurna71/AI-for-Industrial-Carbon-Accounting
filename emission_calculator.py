import pandas as pd
from nlp_extractor import extract_energy_data

def calculate_emissions(text_file, factors_csv='emission_data/emission_factors.csv'):
    # Load emission factors
    df = pd.read_csv(factors_csv)
    factors = {row['source']: row['co2_factor'] for _, row in df.iterrows()}

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
        factor_key = source.replace('_kwh', '').replace('_litres', '').replace('_m3', '')
        co2_factor = factors.get(factor_key, 0)
        emissions = amount * co2_factor
        results[source] = {
            'amount': amount,
            'unit': df[df['source'] == factor_key]['unit'].values[0] if factor_key in df['source'].values else '',
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
