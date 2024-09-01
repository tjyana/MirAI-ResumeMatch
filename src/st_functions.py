import pdfplumber
import streamlit as st
from src.resumematch_functions import compare_resume
from src.pdf_functions import read_resume
from src.scraper_jdpage import scrape_jd


# English version
# ------------------------------------------------------

def title():
    # Title
    title = '''
    [MirAI Fest Entry]
    # :orange[ResumeMatch]✅
    ### Compare a resume to a job description!
    '''
    st.sidebar.markdown(title, unsafe_allow_html=True)


def resume_input():
    # Input: Resume
    st.sidebar.header("Resume")

    # Select input method: Copy and paste text or upload a file
    resume_method = st.sidebar.radio("""Choose Resume input method:""", ("File", "Text"), horizontal = True)

    # Input: Text
    if resume_method == "Text":
        resume_text = st.sidebar.text_area("Enter Resume text")
        if resume_text:
            return resume_text

    # Input: File Upload
    elif resume_method == "File":
        resume_file = st.sidebar.file_uploader("Upload Resume file", type=["pdf", "docx", "txt"])
        if resume_file:
            resume_text = read_resume(resume_file)
            return resume_text


def jd_input():
    # Input: Job Description
    st.sidebar.header("Job Description")

    # Select input method:
    jd_method = st.sidebar.radio("""Choose JD input method:""", ("JD Link", "Text"), horizontal = True)

    # Input: Link
    if jd_method == "JD Link":
        jd_link = st.sidebar.text_input("Enter JD link")
        if jd_link:
            try:
                jd_title, jd_text = scrape_jd(jd_link)
                return jd_title, jd_text
            except Exception as e:
                st.error("Could not retrieve job information from the URL. Please check the URL.")
                return None, None

    # Input: Text
    elif jd_method == "Text":
        jd_text = st.sidebar.text_area("Enter JD text")
        if jd_text:
            jd_title = "Summary"
            return jd_title, jd_text

    return None, None


def submit_button(resume_text, jd_title, jd_text, language):
    if jd_text and resume_text:
        if jd_title == "Summary":
            st.write('Job Description: ', jd_text[0:100] + '...')
        else:
            st.write(f'Job Description: {jd_title}')
        # st.write(f'求人：{jd_title}')
        st.write('レジュメ内容：', resume_text[0:100] + '...')
        st.toast("✅Inputs confirmed! Click 'Match!' to proceed.")
    # Submit button
    if st.sidebar.button("Match!"):
        if jd_text is None:
            st.error('Please enter a valid MoneyForward job description.')
        if resume_text is None:
            st.error('Please enter a valid resume.')
        else:
            output = compare_resume(resume_text, jd_title, jd_text, language)
            return output


# Orchestrating the English version
def UI(language):
    title()
    jd_title, jd_text = jd_input()
    resume_text = resume_input()
    output = submit_button(resume_text, jd_title, jd_text, language)
    return output
