import importlib.resources as pkg_resources
import re
import smtplib
from email.mime.text import MIMEText

import anthropic
import markdown

from gust.error import NoWeeklyGustFound

DATA_DIR = pkg_resources.files("gust.data")


def generate_report(model: str, api_key: str) -> str:
    """
    Generate an offshore wind industry report using the Anthropic API.

    Args:
        model: The Anthropic model identifier to use.
        api_key: The Anthropic API key.

    Returns:
        A weekly gust report in markdown format.

    Raises:
        NoWeeklyGustFound: If the response does not contain a weekly gust section.
    """
    client = anthropic.Anthropic(api_key=api_key)

    with DATA_DIR.joinpath("prompt.md").open() as f:
        prompt = f.read()

    response = client.messages.create(
        model=model,
        max_tokens=8096,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        # Enable web search.
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        temperature=0.1,
    )

    # Collate weekly gust (avoid preamble).
    weekly_gust = ""
    weekly_gust_started = False

    for block in response.content:
        if block.type == "text":
            if "## Weekly Gust" in block.text:
                weekly_gust_started = True

            if weekly_gust_started:
                weekly_gust += block.text

    # Chop out any remaining preamble.
    weekly_gust = re.sub(
        r".*## Weekly Gust", "## Weekly Gust", weekly_gust, flags=re.DOTALL
    )

    if not weekly_gust_started or weekly_gust == "":
        response_text = "".join(
            block.text for block in response.content if block.type == "text"
        )

        NoWeeklyGustFound(f"Weekly gust not found, response text: {response_text}")

    return weekly_gust


def send_report(
    report_text: str, sender: str, sender_password: str, recipient: str
) -> None:
    """
    Send the report as an HTML email via Gmail SMTP.

    Args:
        report_text: The report content in a markdown format.
        sender: The sender's Gmail address.
        sender_password: The sender's Gmail app password.
        recipient: The recipient's email address.
    """
    # Convert markdown to HTML.
    html_body = markdown.markdown(report_text)
    html = f"""
    <html>
    <body style="font-family: sans-serif; max-width: 600px; margin: auto; padding: 20px;">
        {html_body}
    </body>
    </html>
    """

    msg = MIMEText(html, "html")
    msg["Subject"] = "Daily Gust - Offshore Wind News"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, sender_password)
        server.sendmail(sender, recipient, msg.as_string())
