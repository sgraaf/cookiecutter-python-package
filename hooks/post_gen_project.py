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


def possibly_install_uv() -> None:
    if shutil.which("uv") is None:
        # possibly install pipx
        possibly_install_pipx()

        # install uv
        subprocess.run([sys.executable, "-m", "pipx", "install", "uv"], check=False)


def initialize_venv() -> None:
    # create virtual environment and install dependencies
    subprocess.run(["uv", "sync", "--dev"], check=False)


def initialize_git_repository() -> None:
    # initialize Git repository
    subprocess.run(["git", "init", "-b", "main"], check=False)

    # update and install pre-commit hooks
    subprocess.run(["prek", "auto-update"], check=False)
    subprocess.run(["prek", "install", "--install-hooks"], check=False)

    # add files
    subprocess.run(["git", "add", "."], check=False)

    # run nox "cog" and "prek" sessions
    subprocess.run(["prek", "run", "--all-files"], check=False)

    # possibly re-add files
    subprocess.run(["git", "add", "."], check=False)

    # commit
    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            "Initial commit from `cookiecutter-python-package`",
        ],
        check=False,
    )


if __name__ == "__main__":
    # possibly install uv (and pipx)
    possibly_install_uv()
    # create venv and install dependencies
    initialize_venv()
    # perform git initialization
    if "{{ cookiecutter.init_git }}" == "True":
        initialize_git_repository()
