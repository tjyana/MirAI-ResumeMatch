import streamlit as st
import pdfplumber
from src.resumematch_functions import compare_resume
from src.st_functions import read_resume, language_options, UI, resume_input, jd_input, submit_button
from src.st_functions_JP import JP_UI, JP_resume_input, JP_jd_input, JP_submit_button





def main():

    language = language_options()

    # English version
    if language == 'English':
        UI()
        resume_text = resume_input()
        jd_text = jd_input()
        submit_button(resume_text, jd_text)

    # Japanese version
    if language == '日本語':
        JP_UI()
        resume_text = JP_resume_input()
        jd_text = JP_jd_input()
        JP_submit_button(resume_text, jd_text)


    # # Title
    # title = '''
    # [MirAI Fest Entry]
    # # :orange[ResumeMatch]✅
    # ### Compare a resume to a job description!
    # '''
    # st.sidebar.markdown(title, unsafe_allow_html=True)

    # # Resume
    # st.sidebar.header("Resume")

    # # Select input method: Copy and paste text or upload a file
    # resume_method = st.sidebar.radio("""Choose Resume input method:""", ("File", "Text"), horizontal = True)

    # # Input: Text
    # if resume_method == "Text":
    #     resume_text = st.sidebar.text_area("Paste Resume text", height=200)
    # # Input: File Upload
    # elif resume_method == "File":
    #     resume_file = st.sidebar.file_uploader("Upload Resume file", type=["pdf", "docx", "txt"])
    #     if resume_file:
    #         resume_text = read_resume(resume_file)

    # # Input: Job Description
    # st.sidebar.header("Job Description")
    # jd_text = st.sidebar.text_area("Paste JD text", height=200)

    # # Submit button
    # if st.sidebar.button("Submit"):
    #     st.header("Match Results")
    #     output = compare_resume(resume_text, jd_text)
    #     process_inputs(output)



def process_inputs(input1):
    # Function to display the final output
    st.markdown(input1, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
