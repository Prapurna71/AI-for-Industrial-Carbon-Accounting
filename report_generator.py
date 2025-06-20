import os
from fpdf import FPDF
from datetime import datetime
from emission_calculator import calculate_emissions

# Utility to safely handle text encoding issues with PDF
def safe_text(text):
    return str(text).encode('latin-1', 'replace').decode('latin-1')

def generate_pdf_report(text_file, output_path="output_reports/emission_audit_report.pdf"):
    results, total = calculate_emissions(text_file)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, safe_text("Industrial Carbon Emission Audit Report"), ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, safe_text(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"), ln=True, align='C')
    pdf.ln(10)

    # Table Header
    pdf.set_font("Arial", 'B', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(60, 10, safe_text("Source"), 1, 0, 'C', True)
    pdf.cell(30, 10, safe_text("Quantity"), 1, 0, 'C', True)
    pdf.cell(30, 10, safe_text("Unit"), 1, 0, 'C', True)
    pdf.cell(30, 10, safe_text("Factor"), 1, 0, 'C', True)
    pdf.cell(40, 10, safe_text("CO₂ (kg)"), 1, 1, 'C', True)

    # Table Rows
    pdf.set_font("Arial", size=12)
    for source, data in results.items():
        pdf.cell(60, 10, safe_text(source.title()), 1)
        pdf.cell(30, 10, safe_text(data['amount']), 1)
        pdf.cell(30, 10, safe_text(data['unit']), 1)
        pdf.cell(30, 10, safe_text(data['co2_factor']), 1)
        pdf.cell(40, 10, safe_text(data['emissions_kg']), 1, ln=True)

    # Total
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(150, 10, safe_text("Total Emissions"), 1)
    pdf.cell(40, 10, safe_text(f"{total} kg CO₂"), 1, ln=True)

    # Footer note
    pdf.set_font("Arial", size=10)
    pdf.ln(10)
    pdf.multi_cell(0, 10, safe_text(
        "Note: Emissions calculated using standard factors from GHG Protocol. "
        "Please verify with ISO 14064 compliance standards if auditing for certification."
    ))

    # Save PDF
    pdf.output(output_path)
    print(f"✅ PDF report generated: {output_path}")
