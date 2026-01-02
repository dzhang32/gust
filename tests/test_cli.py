import os

import pytest
from click.testing import CliRunner

from gust.cli import cli


@pytest.mark.skipif(
    os.getenv("GITHUB_ACTIONS") == "true", reason="Avoid emails from GHA."
)
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
