import os
from gen.helpers.helper_file import HelperFile


class DjGenerateMessageChannel:


    def invoke(self, full_path):
        self.create_file_init(full_path)
        self.create_message_channel(full_path)
            

    def create_file_init(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "core", "messages")

        content = ""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="__init__.py",
            content=content
        )
        
        
    def create_message_channel(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "core", "messages")
    
        content = f'''import os
import requests
from django.conf import settings

class MessageChannel:
    
    @staticmethod
    def send(text: str, title: str = "Title", is_error: bool = False) -> None:

        url = settings.MESSAGE_CHANNEL_URL
        if not url:
            return

        title = f"{{title}} {{settings.APP_NAME}} {{settings.APP_ENV}}"

        text = text[:500]

        payload = {{
            "embeds": [{{
                "title": title,
                "description": text,
                "color": 0xFF0000 if is_error else 0x00FF00,
            }}]
        }}

        try:
            requests.post(url, json=payload, timeout=5)
        except requests.RequestException:
            pass
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="message_channel.py",
            content=content
        )
