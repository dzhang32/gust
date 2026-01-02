from pathlib import Path



def add_one_file(input_file: Path) -> list[int]:
    """
    Example function that adds one to the input.

    Args:
        input_file: The input file containing one integer per line.

    Returns:
        A list of integers, one for each line in the input file.
    """
    with open(input_file, "r") as f:
        return [add_one(int(line.strip())) for line in f]


def add_one(x: int) -> int:
    """
    Example function that adds one to the input.

    Args:
        x: The input number.

    Returns:
        The input number plus one.
    """

    return x + 1
