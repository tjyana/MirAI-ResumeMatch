import streamlit as st
# import google.generativeai as genai
from dotenv import load_dotenv
import os
from openai import OpenAI

# # for testing locally --------------------------------------
# load_dotenv()
# goog_api_key = os.getenv('GOOGLE_API_KEY')

# # for testing on streamlit share -----------------------------
# goog_api_key = st.secrets['GOOGLE_API_KEY']


# load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')

# for testing on streamlit share -----------------------------
api_key = st.secrets['OPENAI_API_KEY']

def compare_resume(resume_text, jd_text):

    # streamlit
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "You are a HR professional screening resumes."
            },
            {
                "role": "user",
                "content": f"""
                Resume: ```{resume_text}```
                Job Description: ```{jd_text}```
                Given the above resume and job description delineated by ```, identify the skills and qualifications from both.
                Compare them to determine any skill gaps and estimate how qualified the individual is for the job.
                Give a percentage estimating how qualified the individual is for the job.

                Please penalize heavily for any missing mandatory qualifications.
                If the candidate is missing any mandatory qualifications, please score no higher than 40%, and please also give a warning.

                If any of the conditionsa are true, please give warnings for the ones that are true:
                - if candidate is missing mandatory qualifications: "Candidate may be missing mandatory qualifications. Please review carefully."
                - if the candidate has no university degree: "Candidate may not have university degree. Highest education listed is [highest education listed]." (example: if high school diploma is highest mentioned, assume they do not have college degree) (if resume does not mention a university degree, assume they don't have one)
                - if candidate is outside of Japan, please give a warning: "Candidate may be overseas. Beware of hiring timelines and visa eligibility." (assume that their last place of work is their current location)


                Output format should be as below, with each section title in large font. Please fill in the blanks with the appropriate information.
                OUTPUT FORMAT:
                ```
                Estimated qualification percentage:

                Candidate Information
                - Current location of candidate:
                - College degree (Bachelor's or above):
                - Japanese language ability:
                - English language ability:

                Warnings:
                (if mandatory qualifications are missing, give a warning here)
                (if no university degree is not listed, give a warning here)
                (if candidate is not in Japan, give a warning here)

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
                ```


                """
            }
        ]
    )

    print(completion)
    print(completion.choices[0].message)


    return completion.choices[0].message['content']


# def compare_resume(resume_text, jd_text):
#     model = genai.GenerativeModel('gemini-1.5-flash')

#     response = model.generate_content(f"""
#     Resume: ```{resume_text}```
#     Job Description: ```{jd_text}```
#     Given the above resume and job description delineated by ```, identify the skills and qualifications from both.
#     Compare them to determine any skill gaps and estimate how qualified the individual is for the job.
#     Give a percentage estimating how qualified the individual is for the job.

#     Please penalize heavily for any missing mandatory qualifications.
#     If the candidate is missing any mandatory qualifications, please score no higher than 40%, and please also give a warning.

#     If any of the conditionsa are true, please give warnings for the ones that are true:
#     - if candidate is missing mandatory qualifications: "Candidate may be missing mandatory qualifications. Please review carefully."
#     - if the candidate has no university degree: "Candidate may not have university degree. Highest education listed is [highest education listed]." (example: if high school diploma is highest mentioned, assume they do not have college degree) (if resume does not mention a university degree, assume they don't have one)
#     - if candidate is outside of Japan, please give a warning: "Candidate may be overseas. Beware of hiring timelines and visa eligibility." (assume that their last place of work is their current location)


#     Output format should be as below, with each section title in large font. Please fill in the blanks with the appropriate information.
#     OUTPUT FORMAT:
#     ```
#     Estimated qualification percentage:

#     Candidate Information
#     - Current location of candidate:
#     - College degree (Bachelor's or above):
#     - Japanese language ability:
#     - English language ability:

#     Warnings:
#     (if mandatory qualifications are missing, give a warning here)
#     (if no university degree is not listed, give a warning here)
#     (if candidate is not in Japan, give a warning here)

#     Summary:
#     (please give a short summary of candidate persona.
#     example: junior level candidate with 2 years of experience in software engineering, proficient in Python, Java, and C++)

#     Top 3 Skills and qualifications from resume:
#     - skill1
#     - skill2
#     - skill3
#     ...
#     3 main skills and qualifications from job description:
#     - skill1
#     - skill2
#     - skill3
#     ...
#     Skill gaps:
#     - skill1
#     - skill2
#     - skill3
#     ...
#     ```


#     """)

#     answer = response.text

#     return answer
