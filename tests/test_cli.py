from click.testing import CliRunner

from gust.cli import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "--model",
            "gemini-2.5-flash-lite",
        ],
    )

    assert result.exit_code == 0
