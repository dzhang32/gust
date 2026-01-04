import click

from gust.report import generate_report, send_report


@click.command()
@click.option(
    "--model", default="claude-haiku-4-5-20251001", help="Model to use for generation."
)
@click.option(
    "--api-key", envvar="CLAUDE_API_KEY", required=True, help="Claude API key."
)
@click.option(
    "--sender", envvar="GUST_SENDER", required=True, help="Sender email address."
)
@click.option(
    "--sender-password",
    envvar="GUST_SENDER_PASSWORD",
    required=True,
    help="Sender email password.",
)
@click.option(
    "--recipient",
    envvar="GUST_RECIPIENT",
    required=True,
    help="Recipient email address.",
)
def cli(model: str, api_key: str, sender: str, sender_password: str, recipient: str):
    """
    Gust - Generate and send daily offshore wind industry reports.
    """
    gust_report = generate_report(model=model, api_key=api_key)
    send_report(
        report_text=gust_report,
        sender=sender,
        sender_password=sender_password,
        recipient=recipient,
    )
    click.echo("Gust report sent!")


if __name__ == "__main__":
    cli()
