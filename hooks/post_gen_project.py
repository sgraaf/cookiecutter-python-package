import os
import subprocess
import sys

# perform git initialization
if "{{ cookiecutter.init_git }}" == "True":
    subprocess.run(["git", "init", "-b", "main"], check=False)
    subprocess.run(["git", "add", "."], check=False)
    subprocess.run(
        ["git", "commit", "-m", "🍪 Initial commit from `cookiecutter-python-package`"],
        check=False,
    )

# create venv and install dependencies
if "{{ cookiecutter.init_venv }}" == "True":
    subprocess.run([sys.executable, "-m", "venv", ".venv"], check=False)
    if os.name == "posix":
        venv_executable = r".venv/bin/python"
    else:
        venv_executable = r".venv\Scripts\python"
    subprocess.run(
        [
            venv_executable,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
            "setuptools",
            "wheel",
            "flit",
        ],
        check=False,
    )
    # install dependencies
    subprocess.run([venv_executable, "-m", "flit", "install", "--symlink"], check=False)
    # install pre-commit hooks
    subprocess.run(["pre-commit", "install"], check=False)
