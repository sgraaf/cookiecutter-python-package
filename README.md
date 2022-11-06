# cookiecutter-python-package

[![Supported Python Versions](https://img.shields.io/badge/python-3.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11-blue)](https://github.com/OutdoorXL/cookiecutter-python)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

A [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating a new Python package.

See https://github.com/sgraaf/cookiecutter-python-package-demo for a demo of this template.

## Usage

```shell
cookiecutter gh:sgraaf/cookiecutter-python-package
```

## Features

-   Code formatting with [isort](https://pycqa.github.io/isort/), [Black](https://black.readthedocs.io/en/stable/) and [Prettier](https://prettier.io/)
-   Automated Python syntax upgrades with [pyupgrade](https://github.com/asottile/pyupgrade)
-   Linting with [Flake8](https://flake8.pycqa.org/en/stable/)
-   Static type-checking with [mypy](http://www.mypy-lang.org/)
-   Testing with [pytest](https://docs.pytest.org/en/stable/index.html)
-   Continuous Integration with [GitHub Actions](https://github.com/features/actions)
-   Documentation with [Sphinx](https://www.sphinx-doc.org/en/master/), [MyST](https://myst-parser.readthedocs.io/en/latest/), and [Read the Docs](https://readthedocs.org/) using the [Furo](https://pradyunsg.me/furo/) theme
-   Automated release builds and uploads to [PyPI](https://pypi.org/)

This template supports Python 3.7, 3.8, 3.9, 3.10 and 3.11.
