import importlib.resources as pkg_resources
import re
import smtplib
from email.mime.text import MIMEText

import anthropic
import markdown

DATA_DIR = pkg_resources.files("gust.data")


def generate_report(model: str, api_key: str) -> str:
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

    return weekly_gust


def send_report(
    report_text: str, sender: str, sender_password: str, recipient: str
) -> None:
    # Convert markdown to HTML
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
