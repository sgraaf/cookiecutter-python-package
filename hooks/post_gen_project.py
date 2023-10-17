import shutil
import subprocess
import sys


def possibly_install_pipx() -> None:
    if shutil.which("pipx") is None:
        # install pipx
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--user", "pipx"], check=False
        )
        # add pipx to PATH
        subprocess.run([sys.executable, "-m", "pipx", "ensurepath"], check=False)


# perform git initialization
if "{{ cookiecutter.init_git }}" == "True":
    # initialize Git repository
    subprocess.run(["git", "init", "-b", "main"], check=False)

    # possibly install pre-commit (and pipx)
    if shutil.which("pre-commit") is None:
        # possibly install pipx
        possibly_install_pipx()

        # install pre-commit
        subprocess.run(
            [sys.executable, "-m", "pipx", "install", "pre-commit"], check=False
        )

    # install and update pre-commit hooks
    subprocess.run(["pre-commit", "install"], check=False)
    subprocess.run(["pre-commit", "autoupdate"], check=False)
    subprocess.run(["pre-commit", "install", "--install-hooks"], check=False)

    # add and commit
    subprocess.run(["git", "add", "."], check=False)
    subprocess.run(
        ["git", "commit", "-m", "🍪 Initial commit from `cookiecutter-python-package`"],
        check=False,
    )

# create venv and install dependencies
if "{{ cookiecutter.init_venv }}" == "True":
    # possibly install nox (and pipx)
    if shutil.which("nox") is None:
        # possibly install pipx
        possibly_install_pipx()

        # install nox
        subprocess.run([sys.executable, "-m", "pipx", "install", "nox"], check=False)

    # run nox "dev" session
    subprocess.run(["nox", "--session", "dev"], check=False)
