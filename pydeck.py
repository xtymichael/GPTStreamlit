import openai
import streamlit as st

openai.api_key = "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"

def generate_cover_letter(model_engine, personal_info, job_description, length, tone):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=f"{personal_info} {job_description}",
        max_tokens=length,
        n=1,
        stop=None,
        temperature=tone
    )

    message = completions.choices[0].text
    return message

def write_cover_letter(personal_info, job_description, length, tone):
    model_engine = "text-davinci-002"
    message = generate_cover_letter(model_engine, personal_info, job_description, length, tone)
    return message

def main():
    st.title("Cover Letter Generator")
    personal_info = st.text_input("Enter your personal information:")
    job_description = st.text_input("Enter the job description:")
    length = st.slider("Select the desired length of the cover letter:", min_value=50, max_value=500, value=100)
    tone = st.slider("Select the desired tone of the cover letter:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    result = write_cover_letter(personal_info, job_description, length, tone)
    st.write("Generated Cover Letter:")
    st.write(result)
    if st.button("Save cover letter"):
        file = st.file_downloader("Download your cover letter", type="txt")
        file.save(result)

if __name__ == '__main__':
    main()
