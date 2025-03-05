from fpdf import FPDF

def generate_pdf_report(candidate_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Resume Analysis Report", ln=True, align="C")

    for key, value in candidate_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(f"reports/{candidate_data['name']}_report.pdf")
