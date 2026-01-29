"""{{ cookiecutter.short_description }}"""


def add_one(x: int) -> int:
    """Add one to the input.

    Args:
        x: The input.

    Returns:
        The input plus one.

    Example:
        >>> from {{ cookiecutter.package_name }} import add_one
        >>> add_one(1)
        2
    """
    return x + 1
