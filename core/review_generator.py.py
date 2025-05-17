import openai

def generate_response(review_text: str, tone: str, business_name: str = "") -> str:
    prompt = f"""You are an AI assistant helping a small business owner respond to a customer review.
    Tone: {tone.lower()}
    Review: {review_text}
    Sign-off: {business_name if business_name else "the team"}

    Write a friendly, empathetic, and professional response:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
