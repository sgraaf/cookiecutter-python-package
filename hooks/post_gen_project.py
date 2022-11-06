import os
import subprocess
import sys

# perform git initialization
if "{{ cookiecutter.init_git }}" == "True":
    subprocess.run(["git", "init", "-b", "main"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "🍪 Initial commit from `cookiecutter-python-package`"])

# create venv and install dependencies
if "{{ cookiecutter.init_venv }}" == "True":
    subprocess.run([sys.executable, "-m", "venv", ".venv"])
    if os.name == "posix":
        venv_executable = r".venv/bin/python"
    else:
        venv_executable = r".venv\Scripts\python"
    subprocess.run([venv_executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "flit"])
    # install dependencies
    subprocess.run([venv_executable, "-m", "flit", "install", "--symlink"])
    # install pre-commit hooks
    subprocess.run(["pre-commit", "install"])
