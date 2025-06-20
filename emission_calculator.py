import pandas as pd
from nlp_extractor import extract_energy_data

def calculate_emissions(text_file, factors_csv='emission_data/emission_factors.csv'):
    df = pd.read_csv(factors_csv)
    factors = {row['source'].lower(): row['co2_factor'] for _, row in df.iterrows()}
    units = {row['source'].lower(): row['unit'] for _, row in df.iterrows()}

    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()
    extracted = extract_energy_data(text)

    results = {}
    total_emissions = 0.0
    for key in extracted:
        amount = extracted[key]
        if '_kwh' in key:
            source = 'electricity'
        elif '_litres' in key and 'diesel' in key:
            source = 'diesel'
        elif '_litres' in key and 'petrol' in key:
            source = 'petrol'
        elif '_m3' in key:
            source = 'natural_gas'
        else:
            continue
        co2_factor = factors.get(source.lower(), 0)
        unit = units.get(source.lower(), '')
        emissions = amount * co2_factor
        results[source] = {
            'amount': amount,
            'unit': unit,
            'co2_factor': co2_factor,
            'emissions_kg': round(emissions, 2)
        }
        total_emissions += emissions

    return results, round(total_emissions, 2)
