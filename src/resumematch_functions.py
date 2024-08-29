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


def JP_compare_resume(resume_text, jd_text, language):
    '''

    Final HTML output version of the function
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

                If any of the conditions are true, please give warnings for the ones that are true:
                - if candidate is missing mandatory qualifications: "必須資格を欠いている可能性があります。慎重にご確認ください。"
                - if the candidate has no university degree: "大学の学位を持っていない可能性があります。記載されている最終学歴は [highest education listed]." (example: if high school diploma is highest mentioned, assume they do not have college degree) (if resume does not mention a university degree, assume they don't have one)
                - if candidate is outside of Japan, please give a warning: "海外にいる可能性があります。採用のタイムラインとビザの適用資格に注意してください。" (assume that their last place of work is their current location)

                Output format should be as below, with each section title in large font.
                Please fill in the blanks with the appropriate information.
                Please make sure output language is in {language}.

                OUTPUT FORMAT:

                <h2>マッチ度: [percentage]</h2>
                <h4>分析:</h4>
                <p>[reason why you gave the percentage]</p>

                <h4>候補者情報</h4>
                <ul>
                    <li>居住地:</li>
                    <li>最終学歴:</li>
                    <li>日本語能力:</li>
                    <li>英語能力:</li>
                </ul>

                <h4>Warnings:</h4>
                <ul>
                    <li>⚠️ (if mandatory qualifications are missing, give a warning here)</li>
                    <li>⚠️ (if no university degree is not listed, give a warning here)</li>
                    <li>⚠️ (if candidate is not in Japan, give a warning here)</li>
                    <li>(if none of the above apply, write "None.")</li>
                </ul>

                <h4>候補者概要:</h4>
                <p>(please give a short summary of candidate's experiences and skills. example: junior level candidate with 2 years of experience in software engineering, proficient in Python, Java, and C++)</p>

                <h4>求めるスキル・経験:</h4>
                <ul>
                    <li>[✅/❌] [Qualification 1]: [What you can tell from the resume]</li>
                    <li>[✅/❌] [Qualification 2]: [What you can tell from the resume]</li>
                    <li>etc.</li>
                </ul>

                <h4>あると望ましいスキル・経験:</h4>
                <ul>
                    <li>[✅/❌] [Nice-to-have 1]: [What you can tell from the resume]</li>
                    <li>[✅/❌] [Nice-to-have 2]: [What you can tell from the resume]</li>
                    <li>etc.</li>
                </ul>

                <h4>不足部分:</h4>
                <p>[write any notable skill gaps here]</p>



                """
            }
        ]
    )

    print(completion)
    print(completion.choices[0].message)

    content = completion.choices[0].message.content

    return content





def compare_resume(resume_text, jd_text, language):
    '''

    Final HTML output version of the function
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
                Please make sure output language is in {language}.

                OUTPUT FORMAT:

                <h2>Estimated Match: [percentage]</h2>
                <h4>Analysis:</h4>
                <p>[reason why you gave the percentage]</p>

                <h4>Candidate Information</h4>
                <ul>
                    <li>Current location:</li>
                    <li>College degree (Bachelor's or above):</li>
                    <li>Japanese language ability:</li>
                    <li>English language ability:</li>
                </ul>

                <h4>Warnings:</h4>
                <ul>
                    <li>⚠️ (if mandatory qualifications are missing, give a warning here)</li>
                    <li>⚠️ (if no university degree is not listed, give a warning here)</li>
                    <li>⚠️ (if candidate is not in Japan, give a warning here)</li>
                    <li>(if none of the above apply, write "None.")</li>
                </ul>

                <h4>Candidate Summary:</h4>
                <p>(please give a short summary of candidate's experiences and skills. example: junior level candidate with 2 years of experience in software engineering, proficient in Python, Java, and C++)</p>

                <h4>Qualifications:</h4>
                <ul>
                    <li>[✅/❌] [Qualification 1]: [What you can tell from the resume]</li>
                    <li>[✅/❌] [Qualification 2]: [What you can tell from the resume]</li>
                    <li>etc.</li>
                </ul>

                <h4>Nice-to-have:</h4>
                <ul>
                    <li>[✅/❌] [Nice-to-have 1]: [What you can tell from the resume]</li>
                    <li>[✅/❌] [Nice-to-have 2]: [What you can tell from the resume]</li>
                    <li>etc.</li>
                </ul>

                <h4>Skill gaps:</h4>
                <p>[write any notable skill gaps here]</p>



                """
            }
        ]
    )
