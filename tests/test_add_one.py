from gust.add_one import add_one, add_one_file


from pathlib import Path



def test_add_one_file(test_data_dir: Path) -> None:
    """
    Test that the add_one_file function works correctly.
    """
    assert add_one_file(test_data_dir / "test_add_one" / "integers.txt") == [2, 3, 4]

def test_add_one() -> None:
    """
    Test that the add_one function works correctly.
    """
    assert add_one(31) == 32