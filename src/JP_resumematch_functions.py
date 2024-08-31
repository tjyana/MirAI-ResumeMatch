import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# # for testing locally --------------------------------------
# load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY') # create a variable in .env file 'GOOGLE_API_KEY' and add the api key there

# # # for testing on streamlit share -----------------------------
# if api_key != True:
#     api_key = st.secrets['OPENAI_API_KEY']


'''
Function requiring OpenAI API
- compare_resume:
    - main function for main.py
    - 1 resume -> 1 job description
    - compares a resume to a job description and outputs a detailed analysis of the candidate's qualifications
'''

# Load OpenAI API key
api_key = st.secrets['OPENAI_API_KEY']

@st.cache_data
def JP_compare_resume(resume_text, jd_title, jd_text, language):
    '''

    Final HTML output version of the function
    '''

    with st.spinner('ResumeMatching...'):

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

                    If any of the conditions are true, please give warnings for the ones that are true:
                    - if candidate is missing mandatory qualifications: "必須資格を欠いている可能性があります。慎重にご確認ください。"
                    - if resume does not mention a 4-year degree, bachelor's, master's, or PhD, or only mentions associate's degree and/or high school diploma: "大学の学位を持っていない可能性があります。記載されている最終学歴は [highest education listed]."
                    - if candidate is outside of Japan, please give a warning: "海外にいる可能性があります。採用のタイムラインとビザの適用資格に注意してください。" (assume that their last place of work is their current location)
                    - if you cannot confirm candidate fulfills jd language requirements or if resume and job description are in different languages, please give a warning: "言語要件が確認されていません。進行する前に確認してください。"


                    Output format should be as below, with each section title in large font.
                    Please fill in the blanks with the appropriate information.
                    Please make sure output language is in {language}.

                    OUTPUT FORMAT:

                    <h2>マッチ度 [percentage]</h2>

                    <ul>
                        <li>⚠️ (if mandatory qualifications are missing, give a warning here)</li>
                        <li>⚠️ (if resume does not mention a 4-year degree, bachelor's, master's, or PhD, or only mentions associate's degree and/or high school diploma)</li>
                        <li>⚠️ (if candidate is not in Japan, give a warning here)</li>
                        <li>⚠️ (if language requirements are not confirmed, give a warning here)</li>
                    </ul>

                    <h4>求人内容の概要：</h5>
                    <p>{jd_title}: [One sentence summary of the job description.]</p>

                    <h4>履歴書の概要：</h5>
                    <ul>
                        <li>[Summary of the resume in one sentence. Please include years of experience if discernible.]</li>
                        <li><b>Current location:</b> [current location] </li>
                        <li><b>Highest eduation:</b> [highest education listed] [</li>
                        <li><b>Japanese language ability:</b> [Japanese language ability discernible from resume] </li>
                        <li><b>English language ability:</b> [English language ability discernible from resume</li>
                    </ul>

                    <h3>マッチ分析：</h3>
                    [reason why you gave the percentage]

                    <h4>求めるスキル・経験：</h4>
                    <ul>
                        <li>[✅/❌] [Qualification 1]: [What you can tell from the resume]</li>
                        <li>[✅/❌] [Qualification 2]: [What you can tell from the resume]</li>
                        <li>etc.</li>
                    </ul>

                    <h4>あると望ましいスキル・経験：</h4>
                    <ul>
                        <li>[✅/❌] [Nice-to-have 1]: [What you can tell from the resume]</li>
                        <li>[✅/❌] [Nice-to-have 2]: [What you can tell from the resume]</li>
                        <li>etc.</li>
                    </ul>





                    """
                }
            ]
        )

    content = completion.choices[0].message.content

    return content
