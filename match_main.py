import streamlit as st
from src.fit_functions import compare_resume
from src.match_functions import match_resume
from dotenv import load_dotenv
import re
import os

# load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')

# additional features:
# job match mode: take resume input > compare to JD database and find best matches
# pdf upload: upload resume and JD as pdfs


def main():
    # Title
    st.sidebar.title("ResumeMatch")
    st.sidebar.write("""Fill in your resume info to see which job matches you best.""")

    # Input fields
    resume_text = st.sidebar.text_area("Resume Information", height=200)
    # jd_text = st.sidebar.text_area("Job Description", height=200)

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        st.session_state.resume_text = resume_text
        # st.session_state.jd_text = jd_text
        st.header("You might be a good fit for these jobs:")
        output = match_resume(resume_text)
        process_inputs(output, resume_text)


def process_inputs(output, resume_text):
    # Function to display the final output:
    # Top 3 job matches plus estimated qualification percentage

    for i, job in enumerate(output, 1):
        st.write(f"{i}: {job['Title']}")
        comparison = compare_resume(resume_text, job['Job Description'])
        pattern = r'Estimated qualification percentage: \d+%'
        match = re.search(pattern, comparison)
        if match:
            st.write(match.group(0))
        else:
            st.write("")
        st.write("")






if __name__ == "__main__":
    main()
