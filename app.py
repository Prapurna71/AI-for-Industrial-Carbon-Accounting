import streamlit as st
import os
from PIL import Image
from ocr_engine import extract_text_from_image
from nlp_extractor import extract_energy_data
from emission_calculator import calculate_emissions
from report_generator import generate_pdf_report

st.set_page_config(page_title="AI Carbon Audit", layout="centered")
st.title("🧾 AI for Industrial Carbon Accounting")

uploaded_file = st.file_uploader("📤 Upload Industrial Invoice (JPG/PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Save uploaded file to invoices folder
    invoices_dir = "invoices"
    os.makedirs(invoices_dir, exist_ok=True)
    file_path = os.path.join(invoices_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Invoice uploaded!")

    # Step 1: OCR
    st.info("🔍 Running OCR...")
    extracted_text = extract_text_from_image(file_path)
    text_file_path = f"extracted_text/{uploaded_file.name}.txt"
    with open(text_file_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    # Step 2: NLP + Emission Calc
    st.info("🤖 Extracting data + calculating emissions...")
    results, total = calculate_emissions(text_file_path)

    st.success("✅ Emission analysis complete!")

    st.subheader("🌍 Carbon Emission Summary")
    for key, data in results.items():
        st.write(f"**{key}**: {data['amount']} {data['unit']} × {data['co2_factor']} → {data['emissions_kg']} kg CO2")

    st.write(f"### 🟢 **Total Emissions: {total} kg CO2**")

    # Step 3: Generate PDF
    report_path = f"output_reports/{uploaded_file.name}_report.pdf"
    generate_pdf_report(text_file_path, output_path=report_path)

    with open(report_path, "rb") as f:
        st.download_button("📄 Download PDF Report", f, file_name="carbon_audit_report.pdf")
