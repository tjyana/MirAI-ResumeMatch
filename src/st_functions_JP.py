import pdfplumber
import streamlit as st
from src.resumematch_functions import JP_compare_resume
from src.pdf_functions import read_resume
from src.scraper_jdpage import scrape_jd






# Japanese version
# ------------------------------------------------------

def JP_UI():
    # Title
    title = '''
    【みんなのMirAIフェス】
    # :orange[ResumeMatch]✅
    ### AIによる履歴書と求人票のマッチング！
    '''
    st.sidebar.markdown(title, unsafe_allow_html=True)


def JP_resume_input():
    # Input: Resume
    st.sidebar.header("Resume")

    # Select input method: Copy and paste text or upload a file
    resume_method = st.sidebar.radio("""履歴書の入力方法を選択""", ("ファイル", "テキスト"), horizontal = True)

    # Input: Text
    if resume_method == "テキスト":
        resume_text = st.sidebar.text_area("履歴書のテキストを入力", height=200)
        return resume_text
    # Input: File Upload
    elif resume_method == "ファイル":
        resume_file = st.sidebar.file_uploader("履歴書ファイルをアップロード", type=["pdf", "docx", "txt"])
        if resume_file:
            resume_text = read_resume(resume_file)
            return resume_text


# def JP_jd_input():
#     # Input: Job Description
#     st.sidebar.header("求人票")
#     jd_text = st.sidebar.text_area("求人内容を貼り付けてください", height=200)
#     return jd_text

def JP_jd_input():
    # Input: Job Description
    st.sidebar.header("求人票")

    # Select input method: Copy and paste text or upload a file
    jd_method = st.sidebar.radio("""求人内容の入力方法を選択""", ("URL", "テキスト"), horizontal = True)

    # Input: Text
    if jd_method == "Text":
        jd_text = st.sidebar.text_area("求人内容を入力", height=200)
        return jd_text
    # Input: Link
    elif jd_method == "Link":
        jd_link = st.sidebar.text_area("求人票のURLを入力")
        if jd_link:
            jd_text = scrape_jd(jd_link)
            return jd_text


def JP_submit_button(resume_text, jd_text, language):
    # Submit button
    if st.sidebar.button("Match!"):
        st.header("結果")
        output = JP_compare_resume(resume_text, jd_text, language)
        return output
