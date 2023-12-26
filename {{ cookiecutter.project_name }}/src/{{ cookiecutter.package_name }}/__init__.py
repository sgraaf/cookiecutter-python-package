"""{{ cookiecutter.short_description }}"""

__version__ = "{{ cookiecutter.version }}"


def add_one(x: int) -> int:
    """Add one to the input.

    Example:
        >>> from {{ cookiecutter.package_name }} import add_one
        >>> add_one(1)
        2

    Args:
        x: The input.

    Returns:
        The input plus one.
    """
    return x + 1
