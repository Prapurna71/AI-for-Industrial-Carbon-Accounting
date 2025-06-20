import streamlit as st
import os
from PIL import Image
from ocr_engine import extract_text_from_image
from nlp_extractor import extract_energy_data
from emission_calculator import calculate_emissions
from report_generator import generate_pdf_report

# Configure Streamlit page
st.set_page_config(page_title="AI Carbon Audit", layout="centered")
st.title("🧾 AI for Industrial Carbon Accounting")

# Create upload folder if not exist
os.makedirs("uploads", exist_ok=True)

# Upload invoice
uploaded_file = st.file_uploader("📤 Upload Industrial Invoice (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Save uploaded file to uploads/
    image_path = os.path.join("uploads", uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Invoice uploaded successfully.")

    # Extract text using OCR
    with st.spinner("🔍 Extracting text with OCR..."):
        extracted_text = extract_text_from_image(image_path)

    # Display extracted text
    st.subheader("📝 Extracted Invoice Text")
    st.text(extracted_text)

    # Save extracted text to file
    txt_path = os.path.join("extracted_text", uploaded_file.name + ".txt")
    os.makedirs("extracted_text", exist_ok=True)
    with open(txt_path, "w", encoding='utf-8') as f:
        f.write(extracted_text)

    # Calculate emissions
    results, total = calculate_emissions(txt_path)

    # Display emission results
    st.subheader("🌍 CO₂ Emission Summary")
    for k, v in results.items():
        st.write(f"**{k}** → {v['amount']} {v['unit']} × {v['co2_factor']} = **{v['emissions_kg']} kg CO₂**")

    st.success(f"🟢 Total Emissions: {total} kg CO₂")

    # Generate PDF report
    output_path = os.path.join("output_reports", uploaded_file.name + "_report.pdf")
    os.makedirs("output_reports", exist_ok=True)
    generate_pdf_report(txt_path, output_path)

    with open(output_path, "rb") as f:
        st.download_button("📄 Download Emission PDF Report", f, file_name="emission_report.pdf")

