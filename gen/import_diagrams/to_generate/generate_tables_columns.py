import os
import re
import html
import xml.etree.ElementTree as ET

from dotenv import load_dotenv
from gen.helpers.helper_columns import parse_columns_input
from gen.helpers.helper_print import capitalize_camel_case, dd, input_with_validation, print_header_list
from gen.helpers.helper_string import convert_word
from gen.import_diagrams.helpers.helper_table_naming import table_to_classes

from gen.php_laravel.to_module_crud.standard_module_crud_php import standard_module_crud_php
from gen.react.to_create_module_crud.standard_module_crud_react import standard_module_crud_react


load_dotenv()
_TAG_RE = re.compile(r"<[^>]+>")


def _clean_value(v: str) -> str:
    if not v:
        return ""

    # decode html entities (&nbsp;, &amp;...)
    v = html.unescape(v)

    # remove html tags
    v = _TAG_RE.sub("", v)

    # normalize spaces/newlines
    v = v.replace("\xa0", " ").replace("\n", " ").strip()

    # collapse multiple spaces
    v = re.sub(r"\s+", " ", v)

    return v


def generate_tables_columns(
    xml_path, 
    excluded_columns, 
    selected_filename=None
):
    
    if selected_filename:
        print(f"✔ 📂 Selecciona un archivo para importar: {selected_filename}")

    tree = ET.parse(xml_path)
    root = tree.getroot()

    excluded = {c.lower() for c in excluded_columns}
    tables = {}
    

    # 1) Tablas (swimlane)
    for cell in root.iter("mxCell"):
        style = cell.attrib.get("style", "")
        if "swimlane" in style:
            table_id = cell.attrib.get("id")
            table_name = _clean_value(cell.attrib.get("value", "unknown_table"))
            if table_id:
                tables[table_id] = {"name": table_name, "columns": []}

    # 2) Columnas
    for cell in root.iter("mxCell"):
        parent_id = cell.attrib.get("parent")
        value = _clean_value(cell.attrib.get("value"))

        if not value or parent_id not in tables:
            continue

        style = cell.attrib.get("style", "")
        if "swimlane" in style:
            continue

        if value.lower() in excluded:
            continue

        tables[parent_id]["columns"].append(value)
    
    
    
    php_full_path = input_with_validation(
        "Proyecto",
        os.getenv("DEFAULT_PATH_CRUD_PHP")
    )
    
    php_namespace = input_with_validation(
        "Namespace (ERP / API / INVOICES)", 
        "API"
    )
    
    php_version_api = input_with_validation(
        "Versión API", 
        "V1"
    )
    
    # react_full_path = input_with_validation(
    #     "Proyecto [React - /Users/dorian/ReactProjects/app-1/ ]",
    #     "/Users/dorian/ReactProjects/app-1/"
    # )
    
    
    
    print_header_list()

    # 3) Output con tu formato
    for table in tables.values():
        table_name = table["name"]
        singular_class, plural_class = table_to_classes(table_name)

        print(f"📄 Table: {table_name} - {singular_class} - {plural_class}")
        cols = table["columns"]
        
        ##dd(cols)
        
        input_columns = " ".join(cols) if cols else ""
        
        ##dd(columns)
        
        print("Columns:", input_columns)
        print()
        
        
        ## Generate CRUD
        columns = parse_columns_input(input_columns)
        standard_module_crud_php(
            php_full_path,
            php_namespace,
            php_version_api,
            singular_class,
            plural_class,
            columns
        )
        