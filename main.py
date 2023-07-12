import streamlit as st
import openai


# Set up OpenAI API credentials
openai.api_key = "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"

# Define the function to generate interview questions
def generate_interview_questions(resume_text):
    prompt = "Based on the provided resume, generate interview questions for the candidate:\n\nResume: " + resume_text + "\n\nQuestion:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=5,
        stop=None,
        temperature=0.7
    )
    questions = [choice['text'].strip() for choice in response.choices]
    return questions

# Define the function to analyze the resume and job description
def analyze_resume(job_description, resume_text):
    prompt = "Based on the provided job description and resume, analyze the resume and provide feedback:\n\nJob Description: " + job_description + "\n\nResume: " + resume_text + "\n\nFeedback:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    feedback = response.choices[0].text.strip()
    return feedback

# Streamlit interface
st.title("Resume to Interview Question Generator and Resume Analysis")

# Resume input
resume = st.text_area("Enter the resume text here:")

# Job description input
job_description = st.text_area("Enter the job description here:")

# Generate interview questions button
if st.button("Generate Interview Questions"):
    if resume:
        questions = generate_interview_questions(resume)
        st.header("Generated Interview Questions:")
        for i, question in enumerate(questions):
            st.subheader(f"Question {i+1}:")
            st.write(question)
    else:
        st.error("Please enter a resume before generating interview questions.")

# Analyze resume button
if st.button("Analyze Resume"):
    if job_description and resume:
        feedback = analyze_resume(job_description, resume)
        st.header("Resume Analysis Feedback:")
        st.write(feedback)
    else:
        st.error("Please enter both the job description and resume for analysis.")
