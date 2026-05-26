import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_postman(full_path, project_name, domain_name):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "SCRIPTS")
    file_path = os.path.join(folder_path, "API-" + project_name + ".postman.collection.json")

    os.makedirs(folder_path, exist_ok=True)


    content = r"""{
	"info": {
		"_postman_id": "c45bcd65-d68b-4fbe-a0b6-b87a5632cbff",
		"name": "API",
		"description": "Api Rest Full \n\nApi URL:\n\n[https://__PROJECT_NAME__/api/v1/](https://__PROJECT_NAME__/api/v1/)\n\nEstructura principales de ENDPOINT para la gestión:\n\n- base_url/list\n- base_url/list-paginate\n- base_url/list/paginate?filter=company\n- base_url/show/id\n- base_url/store\n- base_url/update\n- base_url/destroy",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "5599797",
		"_collection_link": "https://warped-satellite-11290.postman.co/workspace/__DOMAIN_NAME__~ae865b4b-fd0c-416a-bcd9-0c9108578f23/collection/5599797-c45bcd65-d68b-4fbe-a0b6-b87a5632cbff?action=share&source=collection_link&creator=5599797"
	},
	"item": [
		{
			"name": "Authentication",
			"item": [
				{
					"name": "Restore Password",
					"item": [
						{
							"name": "forgot Password",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "email",
											"value": "admin@__DOMAIN_NAME__",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "{{base_url}}auth/password/email/",
									"host": [
										"{{base_url}}auth"
									],
									"path": [
										"password",
										"email",
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "Restore Password",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "token",
											"value": "o3T8UOouVBmNYe48QEGgE7AGYycgxHlKA5ySHitAnaGa50bHtVdu57Pp2Kv6",
											"type": "text"
										},
										{
											"key": "password",
											"value": "pepepe",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "{{base_url}}auth/password/restore/",
									"host": [
										"{{base_url}}auth"
									],
									"path": [
										"password",
										"restore",
										""
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "login",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"let response = JSON.parse(pm.response.text());",
									"pm.collectionVariables.set(\"token_api\", response.token);"
								],
								"type": "text/javascript",
								"packages": {}
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text",
								"uuid": "b15de912-b133-4bec-b152-12fb3986d9eb"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "email",
									"value": "admin@__DOMAIN_NAME__",
									"description": "Email usuario admin",
									"type": "text"
								},
								{
									"key": "password",
									"value": "Tailandia2026",
									"description": "Password de usuario admin",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}auth/login/",
							"host": [
								"{{base_url}}auth"
							],
							"path": [
								"login",
								""
							]
						},
						"description": "This HTTP POST request is used to authenticate and login a user. The request is sent to the endpoint `{{base_url}}auth/login`.\n\nThe request does not require any specific parameters to be passed in the body or as query parameters.\n\nThe response received after a successful login has a status code of 201. The response body contains the following properties:\n\n- `message`: A string that may contain additional information or a success message.\n- `token`: A string representing the authentication token for the logged-in user.\n- `token_type`: A string representing the type of the authentication token.\n- `success`: A boolean value indicating whether the login was successful or not.\n- `status_code`: An integer representing the status code of the response.\n    \n\nPlease note that the actual values of the `message`, `token`, and `token_type` properties may vary based on the specific implementation of the authentication system.\n\nTo use this endpoint, send an HTTP POST request to `{{base_url}}auth/login` without any request parameters. The response will contain the authentication token if the login is successful.\n\nExample:\n\n```\nPOST {{base_url}}auth/login\n\n ```\n\nResponse:\n\n```\nStatus: 201\n{\n  \"message\": \"\",\n  \"token\": \"\",\n  \"token_type\": \"\",\n  \"success\": true,\n  \"status_code\": 0\n}\n\n ```"
					},
					"response": []
				},
				{
					"name": "show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text",
								"uuid": "8ee147c7-1c9c-4f5a-b54c-019db3f93c1c"
							},
							{
								"key": "Authorization",
								"value": "Token {{token_api}}",
								"type": "text",
								"uuid": "28341df2-dcf3-4211-bcfa-9def40c0c15c"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}auth/user/",
							"host": [
								"{{base_url}}auth"
							],
							"path": [
								"user",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "logout",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text",
								"uuid": "d326a93e-c13f-4d10-b0ac-e7b618d44a2b"
							},
							{
								"key": "Authorization",
								"value": "Token {{token_api}}",
								"type": "text",
								"uuid": "ceb2cd55-8f07-4f33-b225-aa776f852e8e"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}auth/logout/",
							"host": [
								"{{base_url}}auth"
							],
							"path": [
								"logout",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Dev",
			"item": [
				{
					"name": "Test",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{base_url}}dev/test/",
							"host": [
								"{{base_url}}dev"
							],
							"path": [
								"test",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Dashboards",
			"item": [
				{
					"name": "List",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"value": "Token {{token_api}}"
							}
						],
						"url": {
							"raw": "{{base_url}}dashboards/list/",
							"host": [
								"{{base_url}}dashboards"
							],
							"path": [
								"list",
								""
							]
						}
					},
					"response": []
				}
			]
		}
	],
	"event": [
		{
			"listen": "prerequest",
			"script": {
				"type": "text/javascript",
				"exec": [
					""
				]
			}
		},
		{
			"listen": "test",
			"script": {
				"type": "text/javascript",
				"exec": [
					""
				]
			}
		}
	],
	"variable": [
		{
			"key": "base_url",
			"value": "http://__PROJECT_NAME__/api/v1/",
			"type": "string"
		},
		{
			"key": "token_api",
			"value": ""
		}
	]
}
"""


    content = content.replace("__PROJECT_NAME__", project_name)
    content = content.replace("__DOMAIN_NAME__", domain_name)
    
    

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)