import os
from gen.helpers.helper_file import HelperFile


class DjGenerateHttp:
    
    def invoke(self, full_path):
        self.create_file_init(full_path)
        self.create_http(full_path)
    
    
    

    def create_file_init(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "core", "http")

        content = ""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="__init__.py",
            content=content
        )
        
        
        
        
    def create_http(self, full_path):
            """
            Genera el archivo.
            """
    
            folder_path = os.path.join(full_path, "core", "http")
    
            content = f'''import requests
from typing import Optional


class ApiRequest:
    
    def __init__(
        self,
        base_url: str,
        token: Optional[str] = None,
        timeout: int = 300,
    ):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    def _headers(self, extra_headers: dict | None = None) -> dict:
        headers = {{
            "Accept": "application/json",
            "Content-Type": "application/json",
        }}

        if self.token:
            headers["Authorization"] = f"Bearer {{self.token}}"

        if extra_headers:
            headers.update(extra_headers)

        return headers

    def _url(self, path: str) -> str:
        return f"{{self.base_url}}/{{path.lstrip('/')}}"

    def get(self, path: str, params: dict | None = None) -> dict:
        r = requests.get(
            self._url(path),
            params=params,
            headers=self._headers(),
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def post(self, path: str, payload: dict) -> dict:
        r = requests.post(
            self._url(path),
            json=payload,
            headers=self._headers(),
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def put(self, path: str, payload: dict) -> dict:
        r = requests.put(
            self._url(path),
            json=payload,
            headers=self._headers(),
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def delete(self, path: str) -> dict:
        r = requests.delete(
            self._url(path),
            headers=self._headers(),
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

'''
    
            # Crear el archivo
            HelperFile.write(
                folder_path=folder_path,
                file_name="api_request.py",
                content=content
            )