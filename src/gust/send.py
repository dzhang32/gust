import smtplib
from email.mime.text import MIMEText

import markdown


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
