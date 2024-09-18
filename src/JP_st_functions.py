import streamlit as st
from src.JP_resumematch_functions import JP_compare_resume
from src.pdf_functions import read_resume
from src.scraper_jdpage import scrape_jd


# Japanese version
# ------------------------------------------------------

def JP_title():
    # Title
    title = '''
    【みんなのMirAIフェス】
    # :orange[ResumeMatch]✅
    ### AIによる履歴書と求人票のマッチング！
    '''
    st.sidebar.markdown(title, unsafe_allow_html=True)


def JP_resume_input():
    # Input: Resume
    st.sidebar.header("レジュメ")

    # Select input method: File upload or Text
    resume_method = st.sidebar.radio("""履歴書の入力方法を選択""", ("ファイル", "テキスト"), horizontal = True, help="履歴書がない場合はChatGPTで作成し、テキスト入力してください🙏")

    # Input: Text
    if resume_method == "テキスト":
        resume_text = st.sidebar.text_area("レジュメのテキストを入力")
        if resume_text:
            return resume_text

    # Input: File Upload
    elif resume_method == "ファイル":
        resume_file = st.sidebar.file_uploader("レジュメファイルをアップロード", type=["pdf", "docx", "txt"])
        if resume_file:
            resume_text = read_resume(resume_file)
            return resume_text


def JP_jd_input():
    # Input: Job Description
    st.sidebar.header("求人内容")

    # Select input method: Link or Text
    jd_method = st.sidebar.radio("""求人内容の入力方法を選択""", ("求人URL", "テキスト"), horizontal = True)

    # Input: Link
    if jd_method == "求人URL":
        jd_link = st.sidebar.text_input("求人票のURLを入力(マネーフォワードの求人内容)")
        if jd_link:
            try:
                jd_title, jd_text = scrape_jd(jd_link)
                return jd_title, jd_text
            except Exception as e:
                st.error("URLから求人情報を取得できませんでした。URLを確認してください。")
                return None, None

    # Input: Text
    elif jd_method == "テキスト":
        jd_text = st.sidebar.text_area("求人内容をテキスト入力")
        if jd_text:
            jd_title = "概要"
            return jd_title, jd_text

    return None, None


def JP_submit_button(resume_text, jd_title, jd_text, language):
    if jd_text and resume_text:

        # Job description preview
        if jd_title == "概要":
            st.markdown('<b>求人内容: </b>', unsafe_allow_html=True)
            st.write(f'{jd_text[0:80]}...')
        else:
            st.markdown('<b>求人: </b>', unsafe_allow_html=True)
            st.write(f'{jd_title}')

        # Resume preview
        st.markdown('<b>レジュメ内容: </b>', unsafe_allow_html=True)
        st.write(f'{resume_text[0:80]}...')

        # Confirmation message
        st.toast("✅入力が確認できました！「Match!」をクリックしてください。")

    # Submit button
    if st.sidebar.button("ResumeMatch!"):
        if jd_text is None:
            st.error('有効なマネーフォワードの求人内容を入力してください。')
        if resume_text is None:
            st.error('有効なレジュメを入力してください。')
        else:
            output = JP_compare_resume(resume_text, jd_title, jd_text, language)
            return output


# Orchestrating the Japanese version
def JP_UI(language):
    JP_title()
    jd_title, jd_text = JP_jd_input()
    resume_text = JP_resume_input()
    output = JP_submit_button(resume_text, jd_title, jd_text, language)
    return output
