import streamlit as st
import os
from PIL import Image
from ocr_engine import extract_text_from_image
from nlp_extractor import extract_energy_data
from emission_calculator import calculate_emissions
from report_generator import generate_pdf_report

# Setup
st.set_page_config(page_title="AI Carbon Audit", layout="centered")
st.title("🧾 AI for Industrial Carbon Accounting")

uploaded_file = st.file_uploader("📤 Upload Industrial Invoice (JPG/PNG)", type=["jpg", "png"])

if uploaded_file is not None:
    # Save uploaded file
    os.makedirs("uploads", exist_ok=True)
    save_path = os.path.join("uploads", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # OCR
    text = extract_text_from_image(save_path)
    
    # Save extracted text
    os.makedirs("extracted_text", exist_ok=True)
    txt_path = f"extracted_text/{uploaded_file.name}.txt"
    with open(txt_path, "w", encoding='utf-8') as f:
        f.write(text)
    
    st.success("✅ Invoice processed successfully.")
    
    # Emission calculation
    results, total = calculate_emissions(txt_path)
    
    st.subheader("🌍 Emission Summary")
    for k, v in results.items():
        st.write(f"**{k.title()}** → {v['amount']} {v['unit']} × {v['co2_factor']} = {v['emissions_kg']} kg CO₂")
    st.write(f"### 🟢 Total Emissions: {total} kg CO₂")

    # Generate and download report
    output_path = f"output_reports/{uploaded_file.name.replace('.jpg', '').replace('.png', '')}_report.pdf"
    generate_pdf_report(txt_path, output_path)

    with open(output_path, "rb") as f:
        st.download_button("📄 Download Emission Report PDF", f, file_name=os.path.basename(output_path))
