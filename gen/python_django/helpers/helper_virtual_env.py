import os
import platform
import subprocess


def get_venv_python(full_path, conda_env_name=None):
    """
    Retorna la ruta del Python del entorno.
    Primero intenta usar Conda si se pasa conda_env_name.
    Si no, busca .venv como antes.
    """

    if conda_env_name:
        result = subprocess.run(
            ["conda", "run", "-n", conda_env_name, "python", "-c", "import sys; print(sys.executable)"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()

        raise FileNotFoundError(
            f"No se encontró el entorno Conda: {conda_env_name}"
        )

    candidates = []

    if platform.system() == "Windows":
        candidates = [
            os.path.join(full_path, ".venv", "Scripts", "python.exe"),
        ]
    else:
        candidates = [
            os.path.join(full_path, ".venv", "bin", "python"),
            os.path.join(full_path, ".venv", "bin", "python3"),
        ]

    for c in candidates:
        if os.path.isfile(c):
            return c

    raise FileNotFoundError(
        f"No se encontró Python en .venv dentro de:\n{full_path}"
    )