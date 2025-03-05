import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    """Extract text from a given PDF file"""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_experience(text):
    """Extracts years of experience from resume text using regex"""
    experience_years = re.findall(r'(\d+)\s*(?:years?|yrs|YRS|Y.o.e)', text, re.IGNORECASE)
    
    if experience_years:
        return max(map(int, experience_years))  # Get the highest number found
    return 0  # Default to 0 if no experience info found

# ✅ Run this test
if __name__ == "__main__":
    # Sample PDF resume (Place a resume file inside the 'data' folder)
    pdf_path = "data/sample_resume.pdf"

    # Step 1: Extract text
    resume_text = extract_text_from_pdf(pdf_path)
    print("Extracted Resume Text:\n", resume_text[:500])  # Print only first 500 characters

    # Step 2: Extract experience
    experience = extract_experience(resume_text)
    print(f"\nExtracted Experience: {experience} years")
