# 🌍 AI for Industrial Carbon Accounting

This project is an AI-powered web application designed to automate carbon emissions auditing for industries. It extracts fuel and electricity usage from uploaded invoice images using OCR and NLP, calculates CO₂ emissions using standard emission factors, and generates audit reports for sustainability compliance.

---

## 🧠 Features

✅ Upload scanned utility or fuel invoices  
✅ OCR + NLP extract usage data (e.g., kWh, litres)  
✅ CO₂ emission calculation using official emission factors  
✅ Downloadable audit report (PDF)  
✅ Built using Streamlit — accessible via any browser

---

## 📸 Sample Input (Invoice)

Diesel (High Speed) 150 lt ₹92.50
Electricity Usage 4000 kWh ₹6.20
---

## 📊 Sample Output

| Source               | Quantity | Unit   | Factor | Emissions (kg CO₂) |
|----------------------|----------|--------|--------|---------------------|
| Diesel (High Speed)  | 150      | litres | 2.68   | 402.0               |
| Electricity Usage    | 4000     | kWh    | 0.133  | 532.0               |
| **Total**            |          |        |        | **934.0**           |

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/prapurna71/AI-for-Industrial-Carbon-Accounting.git
cd AI-for-Industrial-Carbon-Accounting

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit app
streamlit run app.py


🖥️ Web Deployment (Streamlit Cloud)
You can deploy this app for free via https://streamlit.io/cloud:

Push this repo to GitHub

Go to Streamlit Cloud → “New App”

Select this repo & app.py

Click “Deploy”

A public URL like https://your-name.streamlit.app will be generated!

📁 Folder Structure

📦 AI-for-Industrial-Carbon-Accounting/
├── app.py                     # Main Streamlit UI
├── ocr_engine.py              # Tesseract OCR extraction
├── nlp_extractor.py           # Regex/NLP data extraction
├── emission_calculator.py     # CO₂ computation logic
├── report_generator.py        # PDF generator
├── invoices/                  # Uploaded images
├── extracted_text/            # OCR text output
├── output_reports/            # Final audit reports
├── emission_data/
│   └── emission_factors.csv   # Lookup table of CO₂ factors
├── requirements.txt           # Dependencies
└── README.md

🔍 Requirements
Python 3.8+

Tesseract OCR installed

Streamlit

Pandas, Pillow, pytesseract, fpdf

📌 Emission Factor Sample
csv
source,unit,co2_factor
Diesel (High Speed),litres,2.68
Electricity Usage,kWh,0.133

📄 License
MIT License — Free to use, improve, and share
© 2025 prapurna

🙋‍♀️ Want to Contribute?
Open an issue or submit a pull request on GitHub.

Let’s build a greener planet together 🌿


---

### ✅ Next Step:
1. Copy the above into a file named **`README.md`**
2. Place it in your project root
3. Commit + push it to GitHub

Let me know if you'd like:
- A custom **badge** (like "Deployed on Streamlit")
- A visual chart added to the example output
- Or help deploying right now!

You're all set!
should i add these also
