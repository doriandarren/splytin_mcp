from gen.databases.settings.connection import get_connection
from gen.export_diagrams.main_export_diagrams import create_export_diagrams_by_list
from gen.helpers.helper_string import convert_word


def list_tables_and_columns(host, user, password, database, port=3306, input_tables=None):
    """
    Retrieves and displays all tables along with their columns in the database.
    """

    connection = get_connection(host, user, password, database, port)

    if connection is None:
        print("❌ Failed to connect to the database.")
        return

    cursor = connection.cursor()
    
    list_tables = []
    

    try:
        # Obtener todas las tablas
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()

        # Compatibilidad con PyMySQL usando DictCursor o cursor normal
        tables = {
            list(table.values())[0] if isinstance(table, dict) else table[0]
            for table in result
        }

        # Si el usuario especificó tablas, filtrar solo esas
        if input_tables:
            input_tables_set = set(input_tables)
            tables_to_list = tables.intersection(input_tables_set)
        else:
            tables_to_list = tables

        if not tables_to_list:
            print("❌ No se encontraron las tablas especificadas.")
            return

        # Recorrer y procesar cada tabla seleccionada
        for table_name in tables_to_list:
            
            cursor.execute(f"DESCRIBE `{table_name}`")
            columns = cursor.fetchall()
            
            clean_columns = []

            # Compatibilidad con PyMySQL usando DictCursor o cursor normal
            filtered_columns = []
            for column in columns:
                column_name = column["Field"] if isinstance(column, dict) else column[0]
                
                if column_name not in {"id", "created_at", "updated_at", "deleted_at"}:
                    filtered_columns.append(column_name)
                    clean_columns.append(column_name)

            # Convertir nombre de tabla a singular/plural
            table_name_format = convert_word(table_name)
            
            
            obj_main = {
                "table_name": table_name,
                "columns": clean_columns
            }
            list_tables.append(obj_main)
            

            # Mostrar el resultado
            print(
                f"[{table_name}] {table_name_format['singular']} *** "
                f"{table_name_format['plural']} : {' '.join(filtered_columns)}"
            )
            
        
        print("\n** Tablas y columnas listadas exitosamente. **\n")
        
        create_export_diagrams_by_list(list_tables, database)
        
        

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()