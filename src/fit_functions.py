import streamlit as st

from dotenv import load_dotenv
import os
from openai import OpenAI

'''
Functions requiring OpenAI API

- compare_resume:
    - base function
    - main function for main.py
    - 1 resume -> 1 job description
    - compares a resume to a job description and outputs a detailed analysis of the candidate's qualifications

- match_percentage:
    - main function for match_main.py
    - 1 resume -> many job descriptions
    - compares a resume to 3 job descriptions and outputs an estimated qualification percentage for each job
    - used in a scenario where a candidate is applying to multiple jobs

- fit_sheet:
    - main function for fit_main.py
    - many resumes -> 1 job description
    - compares multiple resumes to a job description and outputs a dataframe with candidate information
    - used in a scenario where a recruiter is screening multiple resumes

'''




# load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')

# for testing on streamlit share -----------------------------
api_key = st.secrets['OPENAI_API_KEY']

# def compare_resume(resume_text, jd_text):

#     # streamlit
#     client = OpenAI()

#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system",
#              "content": "You are a tech recruiter screening resumes."
#             },
#             {
#                 "role": "user",
#                 "content": f"""
#                 Resume: ```{resume_text}```
#                 Job Description: ```{jd_text}```
#                 Given the above resume and job description delineated by ```, identify the skills and qualifications from both.
#                 Compare them to determine any skill gaps and estimate how qualified the individual is for the job.
#                 Give a percentage estimating how qualified the individual is for the job.

#                 Please penalize heavily for any missing mandatory qualifications.
#                 If the candidate is missing any mandatory qualifications, please also give a warning.

#                 If any of the conditionsa are true, please give warnings for the ones that are true:
#                 - if candidate is missing mandatory qualifications: "Candidate may be missing mandatory qualifications. Please review carefully."
#                 - if the candidate has no university degree: "Candidate may not have university degree. Highest education listed is [highest education listed]." (example: if high school diploma is highest mentioned, assume they do not have college degree) (if resume does not mention a university degree, assume they don't have one)
#                 - if candidate is outside of Japan, please give a warning: "Candidate may be overseas. Beware of hiring timelines and visa eligibility." (assume that their last place of work is their current location)


#                 Output format should be as below, with each section title in large font.
#                 Please fill in the blanks with the appropriate information.
#                 Please use new lines appropriately like in the format below.

#                 OUTPUT FORMAT:
#                 ```

#                 ### Candidate Information
#                 - Current location:
#                 - College degree (Bachelor's or above):
#                 - Japanese language ability:
#                 - English language ability:

#                 ### Warnings:
#                 ⚠️(if mandatory qualifications are missing, give a warning here)
#                 ⚠️(if no university degree is not listed, give a warning here)
#                 ⚠️(if candidate is not in Japan, give a warning here)
#                 (if none of the above apply, write "None.")

#                 ## Estimated qualification percentage: [percentage]
#                 ### Analysis:
#                 [reason why you gave the percentage]

#                 ### Candidate Summary:
#                 (please give a short summary of candidate's experiences and skills.
#                 example: junior level candidate with 2 years of experience in software engineering, proficient in Python, Java, and C++)

#                 ### Qualifications:
#                 [✅/❌] [Qualification 1]: [What you can tell from the resume]  \n
#                 [✅/❌] [Qualification 2]: [What you can tell from the resume]  \n
#                 etc.  \n

#                 ### Nice-to-have:
#                 [✅/❌] [Nice-to-have 1]: [What you can tell from the resume]  \n
#                 [✅/❌] [Nice-to-have 2]: [What you can tell from the resume]  \n
#                 etc.  \n

#                 ### Skill gaps:
#                 [write any notable skill gaps here]

#                 ...
#                 ```


#                 """
#             }
#         ]
#     )

#     print(completion)
#     print(completion.choices[0].message)

#     content = completion.choices[0].message.content

#     return content




def compare_resume(resume_text, jd_text):
    '''
    HTML Version of the function
    '''


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


                Output format should be as below, with each section title in large font.
                Please fill in the blanks with the appropriate information.

                OUTPUT FORMAT:

                <h2>Candidate Information</h2>
                <ul>
                    <li>Current location:</li>
                    <li>College degree (Bachelor's or above):</li>
                    <li>Japanese language ability:</li>
                    <li>English language ability:</li>
                </ul>

                <h2>Warnings:</h2>
                <ul>
                    <li>⚠️ (if mandatory qualifications are missing, give a warning here)</li>
                    <li>⚠️ (if no university degree is not listed, give a warning here)</li>
                    <li>⚠️ (if candidate is not in Japan, give a warning here)</li>
                    <li>(if none of the above apply, write "None.")</li>
                </ul>

                <h2>Estimated qualification percentage: [percentage]</h2>
                <h3>Analysis:</h3>
                <p>[reason why you gave the percentage]</p>

                <h3>Candidate Summary:</h3>
                <p>(please give a short summary of candidate's experiences and skills. example: junior level candidate with 2 years of experience in software engineering, proficient in Python, Java, and C++)</p>

                <h3>Qualifications:</h3>
                <ul>
                    <li>[✅/❌] [Qualification 1]: [What you can tell from the resume]</li>
                    <li>[✅/❌] [Qualification 2]: [What you can tell from the resume]</li>
                    <li>etc.</li>
                </ul>

                <h3>Nice-to-have:</h3>
                <ul>
                    <li>[✅/❌] [Nice-to-have 1]: [What you can tell from the resume]</li>
                    <li>[✅/❌] [Nice-to-have 2]: [What you can tell from the resume]</li>
                    <li>etc.</li>
                </ul>

                <h3>Skill gaps:</h3>
                <p>[write any notable skill gaps here]</p>



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
                Please output a dataframe with the following format:
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
