import streamlit as st
import pdfplumber
from src.resumematch_functions import compare_resume, JP_compare_resume
from src.st_functions import read_resume, language_options, UI, resume_input, jd_input, submit_button
from src.st_functions_JP import read_resume, JP_UI, JP_resume_input, JP_jd_input, JP_submit_button


def main():

    language = language_options()

    # English version
    if language == 'English':
        UI()
        resume_text = resume_input()
        jd_text = jd_input()
        output = submit_button(resume_text, jd_text, language)
        if output:
            process_inputs(output)

    # Japanese version
    elif language == '日本語':
        JP_UI()
        resume_text = JP_resume_input()
        jd_text = JP_jd_input()
        output = JP_submit_button(resume_text, jd_text, language)
        if output:
            process_inputs(output)


def process_inputs(input1):
    # Function to display the final output
    st.markdown(input1, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
