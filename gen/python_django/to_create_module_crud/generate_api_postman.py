import os
import json
from gen.helpers.helpers import dd
from helpers.helper_print import print_message, GREEN, CYAN

def generate_api_postman(
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
        columns,
    ):
    """
    Genera el archivo
    """
    
   

    folder_path = os.path.join(full_path, "SCRIPTS")
    file_path = os.path.join(folder_path, f'{singular_name}Collection.json')

    os.makedirs(folder_path, exist_ok=True)
    
    
    # Obtener los nombres de las columnas dinámicamente
    column_names = [column["name"] for column in columns]


    content = {
        "info": {
            "_postman_id": "1e8ef847-456f-4806-9ab0-c4b861fe675d",  # Puedes generar un UUID único si es necesario
            "name": singular_name,
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
            "_exporter_id": "5599797"
        },
        "item": [
            {
                "name": plural_name,
                "item": [
                    {
                        "name": "List",
                        "protocolProfileBehavior": {
                            "disableBodyPruning": True
                        },
                        "request": {
                            "method": "GET",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}/list",
                                "host": [f"{{{{base_url}}}}{plural_name_kebab}"],
                                "path": ["list"]
                            }
                        },
                        "response": []
                    },
                    {
                        "name": "Show",
                        "protocolProfileBehavior": {
                            "disableBodyPruning": True
                        },
                        "request": {
                            "method": "GET",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}/show/1",
                                "host": [f"{{{{base_url}}}}{plural_name_kebab}"],
                                "path": ["show", "1"]
                            }
                        },
                        "response": []
                    },
                    {
                        "name": "Store",
                        "request": {
                            "method": "POST",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "body": {
                                "mode": "formdata",
                                "formdata": [
                                    {"key": column, "value": f"New {column}", "type": "text"}
                                    for column in column_names
                                ]
                            },
                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}/store",
                                "host": [f"{{{{base_url}}}}{plural_name_kebab}"],
                                "path": ["store"]
                            }
                        },
                        "response": []
                    },
                    {
                        "name": "Update",
                        "request": {
                            "method": "PUT",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "body": {
                                "mode": "urlencoded",
                                "urlencoded": [
                                    {"key": column, "value": f"Update {column}", "type": "text"}
                                    for column in column_names
                                ]
                            },
                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}/update/1",
                                "host": [f"{{{{base_url}}}}{plural_name_kebab}"],
                                "path": ["update", "1"]
                            }
                        },
                        "response": []
                    },
                    {
                        "name": "Delete",
                        "request": {
                            "method": "DELETE",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}/delete/1",
                                "host": [f"{{{{base_url}}}}{plural_name_kebab}"],
                                "path": ["delete", "1"]
                            }
                        },
                        "response": []
                    }
                ]
            }
        ]
    }


    try:
        with open(file_path, "w") as f:
            json.dump(content, f, indent=4)
            #f.write(content)
        print_message(f"Archivo generado: {file_path}*************", GREEN)
        
        ##dd("PASAA....")
        
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        


