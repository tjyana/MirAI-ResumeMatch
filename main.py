import streamlit as st
from src.fit_functions import compare_resume
from src.st_functions import read_resume



def main():
    # # Title
    # st.sidebar.write('[MirAI Fest Entry]')
    # st.sidebar.title("ResumeMatch")
    # st.sidebar.subheader("""Compare a resume to a job description.""")

    # title = '''
    # [MirAI Fest Entry]
    # # :orange[ResumeMatch]✅
    # ### Compare a resume to a job description!
    # '''

    title = '''
    <p><strong>[MirAI Fest Entry]</strong></p>
    <p><h1>ResumeMatch✅</h1></p>
    <h4>Compare a resume to a job description!</h4>
    '''

    st.sidebar.markdown(title, unsafe_allow_html=True)

    # Input Fields

    # Resume
    st.sidebar.header("Resume")

    # Select input method: Copy and paste text or upload a file
    resume_method = st.sidebar.radio("""Choose Resume input method:""", ("File", "Text"), horizontal = True)

    # Input: Text
    if resume_method == "Text":
        resume_text = st.sidebar.text_area("Paste Resume text", height=200)
    # Input: File Upload
    elif resume_method == "File":
        resume_file = st.sidebar.file_uploader("Upload Resume file", type=["pdf", "docx", "txt"])

        print('resume_file:', resume_file)

    # Input: Job Description
    st.sidebar.header("Job Description")
    jd_text = st.sidebar.text_area("Paste JD text", height=200)

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        # st.session_state.resume_text = resume_text
        # st.session_state.jd_text = jd_text
        st.header("Match Results")

        if resume_method == "Text":
            output = compare_resume(resume_text, jd_text)
            process_inputs(output)
        elif resume_method == "File":
            resume_text = read_resume(resume_file)
            output = compare_resume(resume_text, jd_text)
            process_inputs(output)


def process_inputs(input1):
    # Function to display the final output
    st.markdown(input1, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
