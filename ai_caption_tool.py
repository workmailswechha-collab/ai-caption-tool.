import streamlit as st
import openai
import os

# Get your OpenAI API key from Streamlit Secrets
openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("AI Instagram Caption Generator")

# Input from user
user_input = st.text_input("Describe your post:")

# Select tone for the caption
tone = st.selectbox("Choose caption tone:", ["Funny", "Emotional", "Motivational", "Casual"])

# Generate caption
if st.button("Generate Caption"):
    prompt = f"Write a {tone} Instagram caption for: {user_input}"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=60
    )
    
    caption = response.choices[0].text.strip()
    st.subheader("Generated Caption:")
    st.write(caption)
