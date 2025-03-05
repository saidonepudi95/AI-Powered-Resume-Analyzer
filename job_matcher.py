from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    """Extracts skills from text using NLP"""
    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return list(set(skills))  # Remove duplicates

def match_resume_to_job(resume_text, job_description):
    """Matches resume skills with job description skills and returns a match percentage"""
    resume_skills = " ".join(extract_skills(resume_text))
    job_skills = " ".join(extract_skills(job_description))
    
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_skills, job_skills])
    similarity = (vectors[0] @ vectors[1].T).toarray()[0][0]
    
    return round(similarity * 100, 2)  # Convert to percentage
