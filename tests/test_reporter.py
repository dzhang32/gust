import os

import pytest
from dotenv import load_dotenv

from gust.report import generate_report


@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") == "true", reason="Avoid token usage.")
def test_report():
    """
    Test that the outputted report is not empty.
    """
    load_dotenv()
    # Use the cheapest model for testing.
    weekly_gust = generate_report(
        model="claude-haiku-4-5-20251001", api_key=os.getenv("CLAUDE_API_KEY")
    )

    assert weekly_gust.startswith("## Weekly Gust")
