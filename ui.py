import streamlit as st
from resume_parser import extract_text_from_pdf
from job_matcher import match_resume_to_job

st.title("AI-Powered Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)
    match_score = match_resume_to_job(resume_text, job_description)
    st.success(f"Match Score: {match_score:.2f}%")
