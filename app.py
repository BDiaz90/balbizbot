import streamlit as st
import openai
from dotenv import load_dotenv
import os
from core.review_generator import generate_response

# Load .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page config
st.set_page_config(
    page_title="BalBizBot – Review Response Assistant",
    page_icon="🤖",
    layout="centered"
)

# --- Header ---
st.markdown("<h1 style='text-align: center;'>🤖 BalBizBot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Craft professional, thoughtful replies to customer reviews in seconds.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Input Section ---
review_text = st.text_area("📄 Paste the customer review below:", height=200)

col1, col2 = st.columns([2, 1])
with col1:
    tone = st.selectbox("✍️ Select tone for your response:", ["Friendly", "Professional", "Apologetic"])
with col2:
    business_name = st.text_input("🧾 Sign-off (optional):", placeholder="e.g. The BalBiz Team")

# --- Generate Response ---
if st.button("🚀 Generate Response"):
    if not review_text.strip():
        st.warning("Please enter a customer review.")
    else:
        with st.spinner("Generating your response..."):
            reply = generate_response(review_text, tone, business_name)
            if reply:
                st.success("✅ Here’s your AI-generated reply:")
                st.text_area("Response", value=reply, height=150)
                st.markdown(
                    f"<button onclick=\"navigator.clipboard.writeText('{reply}')\">📋 Copy to Clipboard</button>",
                    unsafe_allow_html=True
                )
            else:
                st.error("Something went wrong. Please try again.")
