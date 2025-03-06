from flask import Flask, request, jsonify
from resume_parser import extract_text_from_pdf, extract_experience
from job_matcher import match_resume_to_job
import os

app = Flask(__name__)

# ✅ Set the absolute path for resumes folder
RESUME_FOLDER = "D:/AI-Projects/AI-Powered-Resume-Analyzer/data/"
JOB_DESCRIPTION_FOLDER = "D:/AI-Projects/AI-Powered-Resume-Analyzer/job_descriptions/"

@app.route("/")
def home():
    return "Welcome to AI-Powered Resume Analyzer API! Use the /analyze endpoint."

@app.route("/analyze", methods=["POST"])
def analyze_resumes():
    files = request.files.getlist("resumes")  # Get multiple uploaded resume files
    job_title = request.form.get("job_title")  # Get job title

    if not files or len(files) == 0:
        return jsonify({"error": "At least one resume file must be uploaded!"}), 400
    if not job_title:
        return jsonify({"error": "Job title is missing!"}), 400

    # ✅ Load job description using absolute path
    job_file_path = os.path.join(JOB_DESCRIPTION_FOLDER, f"{job_title}.txt")
    if not os.path.exists(job_file_path):
        return jsonify({"error": f"Job description '{job_title}' not found!"}), 400

    with open(job_file_path, "r", encoding="utf-8") as job_file:
        job_description = job_file.read()

    # ✅ Process multiple resumes
    results = []
    for file in files:
        resume_path = os.path.join(RESUME_FOLDER, file.filename)

        # Save uploaded file to resume folder
        file.save(resume_path)

        resume_text = extract_text_from_pdf(resume_path)
        years_experience = extract_experience(resume_text)
        match_score = match_resume_to_job(resume_text, job_description)

        results.append({
            "candidate_name": file.filename,
            "experience_years": years_experience,
            "match_score": f"{match_score}%"
        })

    # ✅ Rank candidates based on match score (Descending Order)
    results.sort(key=lambda x: float(x["match_score"].replace("%", "")), reverse=True)

    return jsonify({"ranked_candidates": results, "message": "Resumes successfully analyzed!"})

if __name__ == "__main__":
    app.run(debug=True)
