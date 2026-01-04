import os

import pytest
from click.testing import CliRunner

from gust.cli import cli


@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") == "true", reason="Avoid token usage.")
def test_cli():
    """
    Test that the CLI command executes successfully.
    """
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "--model",
            "claude-haiku-4-5-20251001",
        ],
    )

    assert result.exit_code == 0
