from pathlib import Path

import pytest


@pytest.fixture
def test_data_dir() -> Path:
    """
    Returns the path to the test data directory.
    """
    return Path(__file__).parent / "data"
