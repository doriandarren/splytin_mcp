from gen.databases.settings.connection import get_connection
from gen.export_diagrams.main_export_diagrams import create_export_diagrams_by_list
from gen.helpers.helper_string import convert_word


def get_foreign_keys(cursor, database, table_name):
    query = """
        SELECT
            kcu.COLUMN_NAME,
            kcu.REFERENCED_TABLE_NAME,
            kcu.REFERENCED_COLUMN_NAME,
            kcu.CONSTRAINT_NAME
        FROM information_schema.KEY_COLUMN_USAGE kcu
        WHERE kcu.TABLE_SCHEMA = %s
          AND kcu.TABLE_NAME = %s
          AND kcu.REFERENCED_TABLE_NAME IS NOT NULL
    """

    cursor.execute(query, (database, table_name))
    result = cursor.fetchall()

    foreign_keys = []

    for fk in result:
        if isinstance(fk, dict):
            foreign_keys.append({
                "column": fk["COLUMN_NAME"],
                "referenced_table": fk["REFERENCED_TABLE_NAME"],
                "referenced_column": fk["REFERENCED_COLUMN_NAME"],
                "constraint_name": fk["CONSTRAINT_NAME"],
            })
        else:
            foreign_keys.append({
                "column": fk[0],
                "referenced_table": fk[1],
                "referenced_column": fk[2],
                "constraint_name": fk[3],
            })

    return foreign_keys


def list_tables_and_columns(host, user, password, database, port=3306, input_tables=None):
    connection = get_connection(host, user, password, database, port)

    if connection is None:
        print("❌ Failed to connect to the database.")
        return

    cursor = connection.cursor()
    list_tables = []

    try:
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()

        tables = {
            list(table.values())[0] if isinstance(table, dict) else table[0]
            for table in result
        }

        if input_tables:
            input_tables_set = set(input_tables)
            tables_to_list = tables.intersection(input_tables_set)
        else:
            tables_to_list = tables

        if not tables_to_list:
            print("❌ No se encontraron las tablas especificadas.")
            return

        for table_name in tables_to_list:

            cursor.execute(f"DESCRIBE `{table_name}`")
            columns = cursor.fetchall()

            foreign_keys = get_foreign_keys(cursor, database, table_name)
            fk_columns = {fk["column"] for fk in foreign_keys}

            #clean_columns = []
            filtered_columns = []


            for column in columns:
                if isinstance(column, dict):
                    column_name = column["Field"]
                    column_type = column["Type"]
                else:
                    column_name = column[0]
                    column_type = column[1]

                if column_name not in {"id", "created_at", "updated_at", "deleted_at"}:
                    #clean_columns.append(column_name)

                    if column_name in fk_columns:
                        filtered_columns.append(f"{column_name}:fk")
                    else:
                        filtered_columns.append(f"{column_name}:{column_type}")



            table_name_format = convert_word(table_name)

            obj_main = {
                "table_name": table_name,
                "columns": filtered_columns,
                "foreign_keys": foreign_keys
            }

            list_tables.append(obj_main)
            
            

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