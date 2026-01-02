from google import genai


def report(model: str, api_key: str) -> str:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents="Explain list comprehensions",
        config={
            "system_instruction": "You are a helpful coding assistant.",
            "max_output_tokens": 1024,
            "temperature": 0.7,
        },
    )

    return response
