from openai import OpenAI
import os
from openai.types import APIError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(review_text: str, tone: str, business_name: str = "") -> str:
    prompt = f"""You are an AI assistant helping a small business owner respond to a customer review.
    Tone: {tone.lower()}
    Review: {review_text}
    Sign-off: {business_name if business_name else "the team"}

    Write a friendly, empathetic, and professional response:"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        if "quota" in str(e).lower() or "insufficient_quota" in str(e).lower():
            return (
                "🚫 Sorry! It looks like we've hit our usage limit for the moment.\n\n"
                "Please try again later or contact support if the issue persists."
            )
        else:
            return f"⚠️ An error occurred while generating your response: {e}"
