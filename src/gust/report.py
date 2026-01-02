import importlib.resources as pkg_resources
import smtplib
from email.mime.text import MIMEText

import markdown
from google import genai

DATA_DIR = pkg_resources.files("gust.data")


def generate_report(model: str, api_key: str) -> str:
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
