from {{ cookiecutter.package_name }} import add_one


def test_add_one():
    assert add_one(1) == 2
