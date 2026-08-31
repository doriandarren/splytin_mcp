import os
import json


def create_postman_structure(base_ruta):
    """
    Crea la estructura de carpetas 'base_ruta/public/Scripts'
    en la ruta especificada.
    """

    postman_folder_path = os.path.join(
        base_ruta,
        "public",
        "Scripts"
    )

    if not os.path.exists(postman_folder_path):
        os.makedirs(postman_folder_path)

        print(
            f"Estructura de carpetas '{postman_folder_path}' creada."
        )

    return postman_folder_path



def generate_index_query_params(columns):
    query_params = [
        {
            "key": "include",
            "value": "",
            "description": "Relationship",
            "disabled": True
        }
    ]

    for column in columns:
        query_params.append({
            "key": f"filter[{column["name"]}]",
            "value": "term",
            "description": f"Filter by {column["name"]}",
            "disabled": True
        })
    
    query_params.append({
        "key": "filter[created_at]",
        "value": "2026-08-01,2026-09-20",
        "description": "Range by created_at",
        "disabled": True
    })
    
        
    query_params.append({
        "key": "filter[updated_at]",
        "value": "2026-08-01,2026-09-20",
        "description": "Range by updated_at",
        "disabled": True
    })
        
    for column in columns:
        query_params.append({
            "key": f"sort",
            "value": f"{column["name"]}",
            "description": f"Sort by {column["name"]}",
            "disabled": True
        })

    
    query_params.append({
        "key": "sort",
        "value": "-created_at",
        "description": "Sort by created_at",
        "disabled": True
    })
    
    return query_params





def generate_postman_file(
    base_ruta,
    singular_name,
    plural_name,
    singular_name_kebab,
    plural_name_kebab,
    columns
):
    """
    Genera un archivo de colección Postman JSON
    basado en los nombres proporcionados.
    """

    postman_folder_path = create_postman_structure(base_ruta)

    file_name = f"{singular_name}Collection.json"

    postman_file_path = os.path.join(
        postman_folder_path,
        file_name
    )

    # Obtener los nombres de las columnas dinámicamente
    column_names = [
        column["name"]
        for column in columns
    ]
    
    
    query_params = generate_index_query_params(columns)

    # Crear estructura Postman
    postman_content = {
        "info": {
            "_postman_id": "1e8ef847-456f-4806-9ab0-c4b861fe675d",
            "name": singular_name,
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
            "_exporter_id": "5599797"
        },

        "item": [
            {
                "name": plural_name,
                "item": [

                    # INDEX
                    {
                        "name": "Index",

                        "protocolProfileBehavior": {
                            "disableBodyPruning": True
                        },

                        "request": {
                            "method": "GET",

                            "header": [
                                {
                                    "key": "Accept",
                                    "value": "application/json",
                                    "type": "text"
                                },
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{token_api}}",
                                    "type": "text"
                                }
                            ],

                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}",
                                "host": [
                                    f"{{{{base_url}}}}{plural_name_kebab}"
                                ],
                                "path": [],
                                "query": {query_params}
                            }
                        },

                        "response": []
                    },

                    # SHOW
                    {
                        "name": "Show",

                        "protocolProfileBehavior": {
                            "disableBodyPruning": True
                        },

                        "request": {
                            "method": "GET",

                            "header": [
                                {
                                    "key": "Accept",
                                    "value": "application/json",
                                    "type": "text"
                                },
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{token_api}}",
                                    "type": "text"
                                }
                            ],

                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}/1",
                                "host": [
                                    f"{{{{base_url}}}}{plural_name_kebab}"
                                ],
                                "path": [
                                    "1"
                                ]
                            }
                        },

                        "response": []
                    },

                    # STORE
                    {
                        "name": "Store",

                        "request": {
                            "method": "POST",

                            "header": [
                                {
                                    "key": "Accept",
                                    "value": "application/json",
                                    "type": "text"
                                },
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{token_api}}",
                                    "type": "text"
                                }
                            ],

                            "body": {
                                "mode": "formdata",

                                "formdata": [
                                    {
                                        "key": column,
                                        "value": f"New {column}",
                                        "type": "text"
                                    }
                                    for column in column_names
                                ]
                            },

                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}",
                                "host": [
                                    f"{{{{base_url}}}}{plural_name_kebab}"
                                ],
                                "path": []
                            }
                        },

                        "response": []
                    },

                    # UPDATE
                    {
                        "name": "Update",

                        "request": {
                            "method": "PUT",

                            "header": [
                                {
                                    "key": "Accept",
                                    "value": "application/json",
                                    "type": "text"
                                },
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{token_api}}",
                                    "type": "text"
                                }
                            ],

                            "body": {
                                "mode": "urlencoded",

                                "urlencoded": [
                                    {
                                        "key": column,
                                        "value": f"Update {column}",
                                        "type": "text"
                                    }
                                    for column in column_names
                                ]
                            },

                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}/1",
                                "host": [
                                    f"{{{{base_url}}}}{plural_name_kebab}"
                                ],
                                "path": [
                                    "1"
                                ]
                            }
                        },

                        "response": []
                    },

                    # DELETE
                    {
                        "name": "Delete",

                        "request": {
                            "method": "DELETE",

                            "header": [
                                {
                                    "key": "Accept",
                                    "value": "application/json",
                                    "type": "text"
                                },
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{token_api}}",
                                    "type": "text"
                                }
                            ],

                            "url": {
                                "raw": f"{{{{base_url}}}}{plural_name_kebab}/1",
                                "host": [
                                    f"{{{{base_url}}}}{plural_name_kebab}"
                                ],
                                "path": [
                                    "1"
                                ]
                            }
                        },

                        "response": []
                    }

                ]
            }
        ]
    }

    # Escribir archivo JSON
    try:
        with open(postman_file_path, "w") as postman_file:
            json.dump(
                postman_content,
                postman_file,
                indent=4
            )

        print(
            f"Archivo de colección Postman "
            f"'{file_name}' creado en: "
            f"{postman_folder_path}"
        )

    except Exception as e:
        print(
            f"Error al crear el archivo de colección "
            f"Postman '{file_name}': {e}"
        )