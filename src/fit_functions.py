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
             "content": "You are a tech recruiter screening resumes."
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
                If the candidate is missing any mandatory qualifications, please also give a warning.

                If any of the conditionsa are true, please give warnings for the ones that are true:
                - if candidate is missing mandatory qualifications: "Candidate may be missing mandatory qualifications. Please review carefully."
                - if the candidate has no university degree: "Candidate may not have university degree. Highest education listed is [highest education listed]." (example: if high school diploma is highest mentioned, assume they do not have college degree) (if resume does not mention a university degree, assume they don't have one)
                - if candidate is outside of Japan, please give a warning: "Candidate may be overseas. Beware of hiring timelines and visa eligibility." (assume that their last place of work is their current location)


                Output format should be as below, with each section title in large font. Please fill in the blanks with the appropriate information.
                OUTPUT FORMAT:
                ```

                ## Candidate Information
                - Current location of candidate:
                - College degree (Bachelor's or above):
                - Japanese language ability:
                - English language ability:

                ## Warnings:
                ⚠️(if mandatory qualifications are missing, give a warning here)
                ⚠️(if no university degree is not listed, give a warning here)
                ⚠️(if candidate is not in Japan, give a warning here)
                ⚠️(if no warnings, write "No warnings.")

                # Estimated qualification percentage: [percentage]
                ## Analysis: [reason why you gave the percentage]

                ## Candidate Summary:
                (please give a short summary of candidate's experiences and skills.
                example: junior level candidate with 2 years of experience in software engineering, proficient in Python, Java, and C++)

                # Qualifications:
                [✅/❌] [Qualification 1]: [What you can tell from the resume]
                [✅/❌] [Qualification 2]: [What you can tell from the resume]
                etc.

                # Nice-to-have:
                [✅/❌] [Nice-to-have 1]: [What you can tell from the resume]
                [✅/❌] [Nice-to-have 2]: [What you can tell from the resume]
                etc.

                Skill gaps: []

                ...
                ```


                """
            }
        ]
    )

    print(completion)
    print(completion.choices[0].message)

    content = completion.choices[0].message.content

    return content



def match_percentage(resume_text, jd_text):

    # streamlit
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "You are a tech recruiter screening resumes."
            },
            {
                "role": "user",
                "content": f"""
                Resume: ```{resume_text}```
                Job Descriptions: ```{jd_text}```

                You will be given 1 resume and 3 job titles along with their descriptions.
                Please compare the resume to each job description and give an estimated qualification percentage for each job.
                Please penalize heavily for any missing mandatory qualifications.

                Please use the below grading rubric to determine the estimated qualification percentage (do NOT output the rubric in the final response):

                ## Candidate Summary:
                (summarize candidate's experiences and skills and compare to persona of job description)

                # Qualifications:
                [✅/❌] [Qualification 1]: [What you can tell from the resume]
                [✅/❌] [Qualification 2]: [What you can tell from the resume]
                etc.

                # Nice-to-have:
                [✅/❌] [Nice-to-have 1]: [What you can tell from the resume]
                [✅/❌] [Nice-to-have 2]: [What you can tell from the resume]
                etc.

                Skill gaps: [consider any notable skill gaps]


                FINAL RESPONSE OUTPUT FORMAT:
                ```
                ## Job 1: [Job Title 1]
                Estimated qualification percentage: [percentage]

                ## Job 2: [Job Title 2]
                Estimated qualification percentage: [percentage]

                ## Job 3: [Job Title 3]
                Estimated qualification percentage: [percentage]
                ```

                """
            }
        ]
    )

    print(completion)
    print(completion.choices[0].message)

    content = completion.choices[0].message.content

    return content



def fit_sheet(resume_text, jd_text):

    # streamlit
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "You are a tech recruiter screening resumes."
            },
            {
                "role": "user",
                "content": f"""
                Resume: ```{resume_text}```
                Job Descriptions: ```{jd_text}```

                You will be given multiple resumes and 1 job description.
                Please compare each resume to each job description and determine the following:
                    - Candidate Name
                    - Location
                    - Highest education level
                    - Japanese language ability
                    - English language ability
                    - Estimated qualification percentage

                Please use the below grading rubric to determine the estimated qualification percentage:
                # Qualifications:
                [✅/❌] [Qualification 1]: [What you can tell from the resume]
                [✅/❌] [Qualification 2]: [What you can tell from the resume]
                etc.
                # Nice-to-have:
                [✅/❌] [Nice-to-have 1]: [What you can tell from the resume]
                [✅/❌] [Nice-to-have 2]: [What you can tell from the resume]
                etc.


                FINAL RESPONSE OUTPUT FORMAT:
                ```
                Please output a spreadsheet with the following format:
                - each row should represent a candidate
                - columns should include the following:
                    - Candidate Name
                    - Location
                    - Highest education level
                    - Japanese language ability
                    - English language ability
                    - Estimated qualification percentage

                Please also output a downloadable link to the spreadsheet.
                ```

                """
            }
        ]
    )

    print(completion)
    print(completion.choices[0].message)

    content = completion.choices[0].message.content

    return content



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
