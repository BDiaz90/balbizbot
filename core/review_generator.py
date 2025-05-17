def generate_response(
    review_text: str,
    tone: str,
    business_name: str = "",
    customer_name: str = "",
    business_type: str = "",
    custom_closing: str = ""
) -> str:
    prompt = f"""
    You are an AI assistant helping a small {business_type.lower()} business respond to a customer review.
    The tone should be {tone.lower()}.

    Review:
    {review_text}

    If the customer name is provided, mention them by name at the beginning.
    Customer name: {customer_name}

    Sign-off with: {business_name if business_name else "the team"}

    If a custom closing sentence is provided, include it at the end.
    Custom closing: {custom_closing}

    Write a warm, professional, and thoughtful response suitable for a public review platform:
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
