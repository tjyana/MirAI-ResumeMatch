import pdfplumber
import streamlit as st
from src.resumematch_functions import compare_resume
from src.pdf_functions import read_resume
from src.scraper_jdpage import scrape_jd


def language_options():
    language = st.sidebar.radio(" ", ['日本語', 'English'], horizontal = True)
    return language


# English version
# ------------------------------------------------------

def UI():
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
        resume_text = st.sidebar.text_area("Paste Resume text", height=200)
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

    # Select input method: Copy and paste text or upload a file
    jd_method = st.sidebar.radio("""Choose JD input method:""", ("Link", "Text"), horizontal = True)

    if jd_method == "Text":
        jd_text = st.sidebar.text_area("Paste JD text", height=200)
        return jd_text


    elif jd_method == "Link":
        jd_link = st.sidebar.text_area("Paste JD link")
        if jd_link:
            jd_text = scrape_jd(jd_link)
            return jd_text


def submit_button(resume_text, jd_text, language):
    # Submit button
    if st.sidebar.button("Match!"):
        st.header("Match Results")
        output = compare_resume(resume_text, jd_text, language)
        return output
