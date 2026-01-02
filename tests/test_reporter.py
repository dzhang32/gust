import os

from dotenv import load_dotenv

from gust.report import report


def test_report():
    load_dotenv()
    news_report = report(
        model="gemini-2.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY")
    )
