import streamlit as st
from huggingface_hub import InferenceClient
import os
MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"
hf_token = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=hf_token)


def ask_ai(prompt):
    try:
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        completion = client.chat.completions.create(
            model=MODEL_ID, 
            messages=messages, 
            max_tokens=1024
        )

        st.markdown(completion.choices[0].message.content)
        
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit App
st.title("AI Assistant")

# User Input
user_prompt = st.text_area("Enter your question or prompt:")

# Ask AI Button
if st.button("Ask AI"):
    with st.spinner("Thinking..."):
        if user_prompt.strip():
            response = ask_ai(user_prompt)
        else:
            st.warning("Please enter a prompt before asking AI.")
