"""Smoke tests for the {{ cookiecutter.friendly_name }} package.

These tests verify that the most critical functionality of the package works.
They are designed to catch major breakage and ensure basic operations succeed.
"""


def test_import() -> None:
    """Test importing the package."""
    import {{ cookiecutter.package_name }}  # noqa: F401, PLC0415
