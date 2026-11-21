import os

from dotenv import load_dotenv
from helpers.helper_columns import HelperColumns
from helpers.helper_string import normalize_project_name
from gen.python_django.helpers.helper_dj_virtual_env import HelperDjVirtualEnv


load_dotenv()


"""
    Importante:

    Para ejecutar:
    # python -m tests.test_dejango

"""
def invoke___():

    full_path = "/Users/dorian/PythonProjects/api.app1.com"
    project_name = normalize_project_name("api.app1.com")


    # Load virtualenv
    venv_python = HelperDjVirtualEnv.get_venv_python(full_path)
    manage_py_path = os.path.join(full_path, "manage.py")

    # venv_python = "/Users/dorian/PythonProjects/api.app1.com/.venv/bin/python"
    # manage_py_path = "/Users/dorian/PythonProjects/api.app1.com/manage.py"




    singular_name = "AgendaUnloading"
    plural_name = "AgendaUnloadings"

    singular_name_kebab = "agenda-unloading"
    plural_name_kebab = "agenda-unloadings"

    singular_name_snake = "agenda_unloading"
    plural_name_snake = "agenda_unloadings"

    singular_first_camel = "agendaUnloading"
    plural_first_camel = "agendaUnloadings"


    columns = HelperColumns.parse_columns_input("name description slug")







    # obj = DjGenerateSee()
    # obj.invoke(
    #     full_path,
    #     project_name,
    #     singular_name,
    #     plural_name,
    #     singular_name_kebab,
    #     plural_name_kebab,
    #     singular_name_snake,
    #     plural_name_snake,
    #     singular_first_camel,
    #     plural_first_camel,
    #     columns
    # )







def invoke():


    full_path = "/Users/dorian/PythonProjects/api.app1.com"
    project_name = normalize_project_name("api.app1.com")
    domain_name = "app1.com"

    password = os.getenv("PASSWORD", "")

    # obj = PythonPostman()
    # obj.invoke(full_path, project_name, domain_name, password)








if __name__ == '__main__':
    invoke()