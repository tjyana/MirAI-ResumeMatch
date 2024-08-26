import streamlit as st
from src.fit_functions import compare_resume
from src.st_functions import read_resume



def main():
    # Title
    st.sidebar.title("ResumeMatch")
    st.sidebar.write("""Compare a resume to a job description.""")

    '''
    Input Fields
    '''
    # Resume
    # resume_text = st.sidebar.text_area("Resume Information", height=200)

    # Select input method: Copy and paste text or upload a file
    resume_method = st.sidebar.radio("""Choose an input method:""", ("Text", "File"))

    # Input: Text
    if resume_method == "Text":
        resume_text = st.sidebar.text_area("Resume Text", height=200)

    # Input: File Upload
    elif resume_method == "File":
        resume_file = st.sidebar.file_uploader("Choose a PDF or DOC file", type=["pdf", "docx", "txt"])
        resume_text = read_resume(resume_file)
        print('resume_file:', resume_file)

    # Input: Job Description
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
