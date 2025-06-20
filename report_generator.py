import pandas as pd
from fpdf import FPDF
from datetime import datetime
from emission_calculator import calculate_emissions

def generate_pdf_report(text_file, output_path="output_reports/emission_audit_report.pdf"):
    results, total = calculate_emissions(text_file)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Industrial Carbon Emission Audit Report", ln=True, align='C')

    # Timestamp
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
    pdf.ln(10)

    # Table header
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, "Source", 1)
    pdf.cell(40, 10, "Quantity", 1)
    pdf.cell(30, 10, "Unit", 1)
    pdf.cell(30, 10, "Factor", 1)
    pdf.cell(40, 10, "CO2 (kg)", 1, ln=True)

    pdf.set_font("Arial", size=12)
    for key, data in results.items():
        pdf.cell(50, 10, key, 1)
        pdf.cell(40, 10, f"{data['amount']}", 1)
        pdf.cell(30, 10, data['unit'], 1)
        pdf.cell(30, 10, str(data['co2_factor']), 1)
        pdf.cell(40, 10, str(data['emissions_kg']), 1, ln=True)

    # Total
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(150, 10, "Total Emissions", 1)
    pdf.cell(40, 10, f"{total} kg CO2", 1, ln=True)

    # Footer
    pdf.set_font("Arial", size=10)
    pdf.ln(10)
    pdf.multi_cell(0, 10, "Note: Emissions calculated using standard factors from GHG Protocol. Please verify with ISO 14064 compliance standards if auditing for certification.")

    # Save PDF
    pdf.output(output_path)
    print(f"✅ PDF report generated: {output_path}")

if __name__ == "__main__":
    generate_pdf_report("extracted_text/invoice1.jpg.txt")
