import streamlit as st
import pdfplumber
from src.resumematch_functions import JP_compare_resume



def read_resume(file):
    '''
    PDFPlumber is a Python library that extracts text, tables, and images from PDF files.
    read_resume function reads the resume file and extracts text from it.
    '''
    if file.type == "text/plain":
        # Read text file
        text = str(file.read(), "utf-8")
    elif file.type == "application/pdf":
        # Extract text from PDF
        with pdfplumber.open(file) as pdf:
            text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # Extract text from DOCX
        doc = docx.Document(file)
        text = '\n'.join(paragraph.text for paragraph in doc.paragraphs if paragraph.text)
    else:
        text = "Unsupported file type"
    return text



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
        resume_text = st.sidebar.text_area("履歴書のテキストを貼り付けて下さい", height=200)
        return resume_text
    # Input: File Upload
    elif resume_method == "File":
        resume_file = st.sidebar.file_uploader("履歴書ファイルをアップロードしてください", type=["pdf", "docx", "txt"])
        if resume_file:
            resume_text = read_resume(resume_file)
            return resume_text


def JP_jd_input():
    # Input: Job Description
    st.sidebar.header("求人票")
    jd_text = st.sidebar.text_area("求人内容を貼り付けてください", height=200)
    return jd_text


def JP_submit_button(resume_text, jd_text, language):
    # Submit button
    if st.sidebar.button("Match!"):
        st.header("結果")
        output = JP_compare_resume(resume_text, jd_text, language)
        return output
