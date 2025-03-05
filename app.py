from flask import Flask, request, jsonify
from resume_parser import extract_text_from_pdf
from job_matcher import match_resume_to_job

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    file = request.files["resume"]
    job_description = request.form["job_description"]
    
    resume_text = extract_text_from_pdf(file)
    match_score = match_resume_to_job(resume_text, job_description)
    
    return jsonify({"match_score": f"{match_score:.2f}%"})

if __name__ == "__main__":
    app.run(debug=True)
