import importlib.resources as pkg_resources

from google import genai

DATA_DIR = pkg_resources.files("gust.data")


def report(model: str, api_key: str) -> str:
    client = genai.Client(api_key=api_key)

    with open(DATA_DIR.joinpath("system_prompt.md")) as f:
        system_prompt = f.read()

    response = client.models.generate_content(
        model=model,
        contents="Create today's daily report on the offshore wind industry.",
        config={
            "system_instruction": system_prompt,
            "max_output_tokens": 1024,
            "temperature": 0.5,
        },
    )

    return response
