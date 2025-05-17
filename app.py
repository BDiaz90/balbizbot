# app.py
import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="BalBizBot – Review Response Generator", layout="centered")
st.title("📝 AI Review Response Generator")
st.markdown("Easily craft thoughtful replies to your business reviews.")

review_text = st.text_area("Paste the customer review below:", height=200)
tone = st.selectbox("Select response tone:", ["Friendly", "Professional", "Apologetic"])
business_name = st.text_input("Optional: Business name or sign-off", placeholder="e.g. The BalBiz Team")

if st.button("Generate Response"):
    if not review_text.strip():
        st.warning("Please enter a customer review to respond to.")
    else:
        with st.spinner("Generating response..."):
            prompt = f"""You are an AI assistant helping a small business owner respond to a customer review.
            The tone should be {tone.lower()}.
            Review: {review_text}
            End the response with '{business_name}' if provided.

            Write a clear, professional, and empathetic response:"""

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                reply = response['choices'][0]['message']['content']
                st.success("Response generated:")
                st.text_area("AI-Generated Response", reply, height=150)
            except Exception as e:
                st.error(f"Error generating response: {e}")
