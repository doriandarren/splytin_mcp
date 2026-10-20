
class HelperPostmanJson:
    """
    Helper para construir colecciones JSON de Postman.
    """

    @staticmethod
    def create_item(
        name,
        method, 
        url, 
        headers=None,
        body=None, 
        events=None, 
        description=None
    ):

        request = {
            "method": method.upper(),
            "header": headers if headers is not None else [],
            "url": url
        }

        if body is not None:
            request["body"] = body

        item = {
            "name": name,
            "request": request,
            "response": []
        }

        if events is not None:
            item["event"] = events

        if description is not None:
            request["description"] = description

        return item


    @staticmethod
    def create_folder(name, items=None):
        return {
            "name": name,
            "item": items if items is not None else []
        }


    @staticmethod
    def create_header(key, value):
        return {
            "key": key,
            "value": value,
            "type": "text"
        }
        

    @staticmethod
    def create_form_field(key, value="", description=None):
        field = {
            "key": key,
            "value": value,
            "type": "text"
        }

        if description is not None:
            field["description"] = description

        return field


    @staticmethod
    def create_form_body(fields):
        return {
            "mode": "formdata",
            "formdata": fields
        }
        
        

    @staticmethod
    def create_raw_body(data):
        import json

        return {
            "mode": "raw",
            "raw": json.dumps(data, indent=4, ensure_ascii=False),
            "options": {
                "raw": {"language": "json"}
            }
        }



    @staticmethod
    def create_test_script(lines):
        return {
            "listen": "test",
            "script": {
                "type": "text/javascript",
                "exec": lines
            }
        }



    @staticmethod
    def create_variable(key, value=""):
        return {
            "key": key,
            "value": value,
            "type": "string"
        }
