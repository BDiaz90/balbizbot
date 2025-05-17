import streamlit as st
import openai
from dotenv import load_dotenv
import os
from core.review_generator import generate_response

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="BalBizBot – Review Responder", layout="centered")
st.title("📝 AI Review Response Generator")
st.markdown("Easily craft thoughtful replies to your business reviews.")

review_text = st.text_area("Paste the customer review below:", height=200)
tone = st.selectbox("Select response tone:", ["Friendly", "Professional", "Apologetic"])
business_name = st.text_input("Optional: Business name or sign-off", placeholder="e.g. The BalBiz Team")

if st.button("Generate Response"):
    if not review_text.strip():
        st.warning("Please enter a customer review.")
    else:
        with st.spinner("Generating..."):
            reply = generate_response(review_text, tone, business_name)
            st.text_area("AI-Generated Response", reply, height=150)