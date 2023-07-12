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

# Streamlit interface
st.title("Resume to Interview Question Generator")

# Resume input
resume = st.text_area("Enter the resume text here:")

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
