import streamlit as st
from src.functions import compare_resume
from dotenv import load_dotenv
import os

# load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')

def main():
    # Title
    st.sidebar.title("QualiScreen")
    st.sidebar.write("""Fill in the fields below to compare a resume to a job description.""")

    # Input fields
    resume_text = st.sidebar.text_area("Resume Information", height=200)
    jd_text = st.sidebar.text_area("Job Description", height=200)

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        st.session_state.resume_text = resume_text
        st.session_state.jd_text = jd_text
        st.header("Fit Score")
        output = compare_resume(resume_text, jd_text)
        process_inputs(output)


def process_inputs(input1):
    # Function to display the final output
    # Process the inputs here
    st.write(" ", input1)


if __name__ == "__main__":
    main()
