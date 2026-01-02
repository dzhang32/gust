import os

from dotenv import load_dotenv

from gust.report import generate_report


def test_report():
    """
    Test that the outputted report is not empty.
    """
    load_dotenv()
    # Use the cheapest model for testing.
    news_report = generate_report(
        model="gemini-2.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY")
    )

    assert news_report != ""
