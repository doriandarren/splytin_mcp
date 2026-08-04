import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import print_header, input_with_validation, print_header_list
from gen.databases.to_list.list_tables import list_tables_and_columns
from gen.databases.to_generate.generate_tables_columns import list_tables_and_columns_and_generate
from dotenv import load_dotenv



load_dotenv()


def main_database():

    print_header("DATABASE")

    database_default = "api_integrations"
    username = 'infinito'
    password = '123456'
    port = 3306

    generator_type = input_with_validation("[1]Listar | [2]Generar: ")
    database_name = input_with_validation("Nombre Basedatos", default_value=database_default)
    input_tables = input("Nombre Tablas [separado por espacio | blanco todos]: ")
    print_header_list();


    password = os.getenv("DATABASE_LOCAL_PASSWORD")
    

    # Convertir input_tables en lista, aunque sea un solo elemento
    input_tables = input_tables.split() if input_tables else []


    if generator_type.lower() == '1':
        list_tables_and_columns(
            "127.0.0.1",
            username,
            password,
            database_name,
            port,
            input_tables
        )


    if generator_type.lower() == '2':
        list_tables_and_columns_and_generate(
            "127.0.0.1",
            username,
            password,
            database_name,
            port,
            input_tables
        )

    pause()


