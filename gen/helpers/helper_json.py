
import os
import json


class HelperJson:

    @staticmethod
    def read(file_path):
        """Lee un archivo JSON y devuelve un diccionario."""

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write(file_path, data):
        """Guarda un diccionario en un archivo JSON."""

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=2,
                ensure_ascii=False
            )
            file.write("\n")

    @staticmethod
    def update(file_path, new_data):
        """Actualiza un JSON conservando las propiedades existentes."""

        data = HelperJson.read(file_path)

        HelperJson.merge(data, new_data)

        HelperJson.write(file_path, data)

    @staticmethod
    def merge(original, new_data):
        """Combina diccionarios de forma recursiva."""

        for key, value in new_data.items():

            if (
                key in original
                and isinstance(original[key], dict)
                and isinstance(value, dict)
            ):
                HelperJson.merge(original[key], value)
            else:
                original[key] = value

        return original
