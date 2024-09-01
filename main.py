import streamlit as st
from src.JP_st_functions import JP_UI
from src.st_functions import UI

def main():

    language = st.sidebar.radio(" ", ['日本語', 'English'], horizontal = True)

    # # English version
    # if language == 'English':
    #     UI()
    #     resume_text = resume_input()
    #     jd_text = jd_input()
    #     output = submit_button(resume_text, jd_text, language)
    #     if output:
    #         process_inputs(output)

    if language == 'English':
        output = UI(language)

    # Japanese version
    elif language == '日本語':
        output = JP_UI(language)

    # # Japanese version
    # elif language == '日本語':
    #     JP_UI()
    #     resume_text = JP_resume_input()
    #     jd_text = JP_jd_input()
    #     output = JP_submit_button(resume_text, jd_text, language)
    #     if output:
    #         process_inputs(output)

    if output:
        st.markdown(output, unsafe_allow_html=True)


# def process_inputs(input1):
#     # Function to display the final output
#     st.markdown(input1, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
