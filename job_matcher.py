import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return list(set(skills))

resume_text = extract_text_from_pdf("data/sample_resume.pdf")
print(extract_skills(resume_text))
