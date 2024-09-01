import streamlit as st
from src.JP_st_functions import JP_UI
from src.st_functions import UI


def main():

    language = st.sidebar.radio(" ", ['日本語', 'English'], horizontal = True)

    # English version
    if language == 'English':
        output = UI(language)

    # Japanese version
    elif language == '日本語':
        output = JP_UI(language)

    # Display the final output
    if output:
        st.markdown(output, unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        if language == 'English':
            st.warning('⬇️Not happy with the results? Search for best fit jobs with JobMatch! ⬇️')
            st.page_link('https://mf-jobmatch.streamlit.app/', label='   👉 JobMatch🕵️ (for Money Forward jobs) 👈')
        elif language == '日本語':
            st.warning('⬇️結果が微妙？JobMatchでベストフィットの求人を探そう！⬇️')
            st.page_link('https://mf-jobmatch.streamlit.app/', label='   👉 JobMatch🕵️ (マネーフォワード求人用) 👈')



if __name__ == "__main__":
    main()
