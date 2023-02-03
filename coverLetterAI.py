import openai
import streamlit as st
from dotenv import load_dotenv
import os

def confiure():
    load_dotenv()

openai.api_key = os.getenv("api_key")

def generate_cover_letter(personal_info, job_title, job_description, length, tone):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a cover letter for a job application for the role of {job_title}. My personal info is {personal_info}. The job description is {job_description}.",
        max_tokens=length,
        n=1,
        stop=None,
        temperature=tone
    )
    message = completions.choices[0].text
    return message

def main():
    confiure()
    st.set_page_config(page_title="AI Cover Letter Generator", page_icon=":guardsman:", layout="wide")
    st.title("AI Cover Letter Generator")
    st.markdown("根据你的能力和公司职位要求，由AI帮你写一封求职信。")

    #User input
    personal_info = st.text_input("Enter your personal information:")
    job_title = st.text_input("Enter Job title:")
    job_description = st.text_input("Enter the job description:")
    length = st.slider("Select the desired length of the cover letter:", min_value=100, max_value=500, value=250, step=50)
    tone = st.slider("Select the desired tone of the cover letter:", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

    

 #   st.write("Generated Cover Letter:")
 #   st.write(result)
    if st.button("Generate your cover letter"):
        result = generate_cover_letter(personal_info, job_title, job_description, length, tone)
        st.success("Cover letter generated!")
        st.markdown(result)
        #st.markdown("Downlaod your cover letter")

        st.download_button(
            label="Download your cover letter",
            data = result,
            file_name='Cover_letter.txt',
        )

if __name__ == '__main__':
    main()
