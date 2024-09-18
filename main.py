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



if __name__ == "__main__":
    main()
