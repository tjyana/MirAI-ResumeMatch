import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# # for testing locally --------------------------------------
# load_dotenv()
# goog_api_key = os.getenv('GOOGLE_API_KEY')

# for testing on streamlit share -----------------------------
goog_api_key = st.secrets['GOOGLE_API_KEY']

def compare_resume(resume_text, jd_text):
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(f"""
    Resume: ```{resume_text}```
    Job Description: ```{jd_text}```
    Given the above resume and job description delineated by ```, identify the skills and qualifications from both.
    Compare them to determine any skill gaps and estimate how qualified the individual is for the job.
    Give a percentage estimating how qualified the individual is for the job.
    For candidate information section, please cite any applicable certifications they have.
    Please penalize heavily for any missing mandatory qualifications.
    If the candidate is missing any mandatory qualifications, please score no higher than 40%, and please also give a warning.

    If any of the conditionsa are true, please give warnings for the ones that are true:
    - if candidate is missing mandatory qualifications: "Candidate is missing mandatory qualifications. Please review carefully."
    - if the candidate has no university degree: "Candidate may not have university degree. Highest education listed is [highest education listed]." (example: if high school diploma is highest mentioned, assume they do not have college degree) (if resume does not mention a university degree, assume they don't have one)
    - if candidate is outside of Japan, please give a warning: "Candidate may be overseas. Beware of hiring timelines and visa eligibility." (assume that their last place of work is their current location)
    - if the position requires Japanese language ability AND the candidate has no Japanese language ability: "Candidate has no Japanese language ability."
    - if the position requires English language ability AND the candidate has no English language ability: "Candidate has no English language ability."

    Output format should be as below, with each section title in large font. Please fill in the blanks with the appropriate information:

    Estimated qualification percentage:

    Warnings:

    Candidate information section

    Current location:

    College degree (Bachelor's or above):

    Japanese language ability:

    English language ability:

    Summary:
    (please give a short summary of candidate persona.
    example: junior level candidate with 2 years of experience in software engineering, proficient in Python, Java, and C++)

    Top 3 Skills and qualifications from resume:
    - skill1
    - skill2
    - skill3
    ...
    3 main skills and qualifications from job description:
    - skill1
    - skill2
    - skill3
    ...
    Skill gaps:
    - skill1
    - skill2
    - skill3
    ...



    """)


    answer = response.text


    return answer
