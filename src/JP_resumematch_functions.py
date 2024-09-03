import streamlit as st
from openai import OpenAI

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

                    please give warnings for items that are true. do not display if not true:
                    - Mandatory Qualifications warning: if 4 or more mandatory qualifications are missing: "Candidate may be missing mandatory qualifications. Please review carefully."
                    - Overseas warning: if candidate is outside of Japan, please give a warning: "Candidate may be overseas. Beware of hiring timelines and visa eligibility." (assume that their last place of work is their current location)
                    - Language Requirements warning: if resume and job description are in different languages, please give a warning: "Language requirements are not confirmed. Please verify before proceeding."

                    Output format should be as below, with each section title in large font.
                    Please fill in the [] with the appropriate information.
                    Please make sure output language is in {language}.

                    OUTPUT FORMAT:

                    <h2>Estimated Match: [percentage]</h2>

                    <h4>Job Description Summary:</h5>
                    <p>{jd_title}: [One sentence summary of the job description.]</p>

                    <h4>Resume Summary:</h5>
                    <ul>
                        <li>[Summary of the resume in one sentence. Please include years of experience if discernible.]</li>
                        <li><b>Current location:</b> [current location] </li>
                        <li><b>Highest eduation:</b> [highest education listed] [</li>
                        <li><b>Japanese language ability:</b> [Japanese language ability discernible from resume] </li>
                        <li><b>English language ability:</b> [English language ability discernible from resume</li>
                    </ul>

                    <ul>
                        <li>⚠️ [Mandatory Qualifications warning if applicable]</li>
                        <li>⚠️ [Overseas warning if applicable]</li>
                        <li>⚠️ [Language Requirements warning if applicable]</li>
                    </ul>

                    <h3>Comparison Analysis:</h3>
                    [reason why you gave the percentage]

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




                    """
                }
            ]
        )

    content = completion.choices[0].message.content

    return content
