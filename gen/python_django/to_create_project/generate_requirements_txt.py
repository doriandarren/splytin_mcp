import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_requirements_txt(full_path, venv_python):
    print_message("Instalando requirements.txt", CYAN)
    run_command(f'"{venv_python}" -m pip freeze > requirements.txt', cwd=full_path)
    print_message("requirements.txt instalado correctamente.", GREEN)

