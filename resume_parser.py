import pdfplumber
import re
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract text from a given PDF file"""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_experience(text):
    """Extracts years of experience from resume text using regex pattern"""
    experience_years = re.findall(r'(\d+)\s*(?:years?|yrs|YRS|Y.o.e)', text, re.IGNORECASE)
    
    if experience_years:
        return max(map(int, experience_years))  # Get the highest number found
    return 0  # Default to 0 if no experience info found

def extract_skills(text):
    """Extracts skills from resume text using NLP"""
    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return list(set(skills))  # Remove duplicates
