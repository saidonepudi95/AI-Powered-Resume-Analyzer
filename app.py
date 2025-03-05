import os
from flask import Flask, request, jsonify
from resume_parser import extract_text_from_pdf, extract_experience
from job_matcher import match_resume_to_job

app = Flask(__name__)

def load_job_description(job_title):
    """Loads job description text from a file"""
    job_file = f"job_descriptions/{job_title}.txt"
    if os.path.exists(job_file):
        with open(job_file, "r", encoding="utf-8") as file:
            return file.read()
    return None

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    file = request.files["resume"]  # Get uploaded resume file
    job_title = request.form["job_title"]  # Get job title to load description

    job_description = load_job_description(job_title)
    if not job_description:
        return jsonify({"error": "Job description not found!"}), 400

    # Extract text from resume
    resume_text = extract_text_from_pdf(file)
    
    # Extract experience
    years_experience = extract_experience(resume_text)
    
    # Calculate match score
    match_score = match_resume_to_job(resume_text, job_description)

    return jsonify({
        "experience_years": years_experience,
        "match_score": f"{match_score}%",
        "message": "Resume successfully analyzed!"
    })

if __name__ == "__main__":
    app.run(debug=True)
