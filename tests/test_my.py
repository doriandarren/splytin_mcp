import os

from gen.helpers.helper_columns import parse_columns_input
from gen.helpers.helper_string import normalize_project_name
from gen.python_django.helpers.helper_virtual_env import get_venv_python
from gen.python_django.to_create_module_crud.dj_generate_api_seeder import DjGenerateApiSeeder



"""
Para ejecutar:
# python -m tests.test_my
"""
def app():
    
    full_path = "/Users/dorian/PythonProjects/api.app1.com"
    project_name = normalize_project_name("api.app1.com")
    
    
    # Load virtualenv
    venv_python = get_venv_python(full_path)
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


    columns = parse_columns_input("name description slug")

    
    
    
    
    
    
    obj = DjGenerateApiSeeder()
    obj.invoke(
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns
    )
    
    




if __name__ == '__main__':
    app()