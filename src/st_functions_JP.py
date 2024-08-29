import streamlit as st

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


def JP_submit_button(resume_text, jd_text):
    # Submit button
    if st.sidebar.button("Match!"):
        st.header("結果")
        output = compare_resume(resume_text, jd_text)
        process_inputs(output)
