import os
import re

from helpers.helper_file import HelperFile


class HelperReactTsIndexCss:

    @staticmethod
    def update_lines(full_path, replacements):
        """
        Actualiza variables CSS según su orden de aparición.

        Ejemplo:
            "--background": [
                "oklch(1 0 0)",       # Primera aparición (:root)
                "oklch(0.145 0 0)",   # Segunda aparición (.dark)
            ]
        """

        main_path = os.path.join(full_path, "src", "index.css")

        if not os.path.isfile(main_path):
            raise FileNotFoundError(
                f"El archivo no existe: {main_path}"
            )

        with open(main_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content

        for property_name, values in replacements.items():

            pattern = re.compile(
                rf"^([ \t]*{re.escape(property_name)}[ \t]*:[ \t]*)"
                rf"([^;\r\n]*)(;)",
                re.MULTILINE,
            )

            matches = list(pattern.finditer(new_content))

            if len(matches) != len(values):
                raise ValueError(
                    f"{property_name}: se esperaban {len(values)} "
                    f"apariciones, pero se encontraron {len(matches)}."
                )

            index = 0

            def replace_value(match):
                nonlocal index

                new_value = values[index]
                index += 1

                return (
                    f"{match.group(1)}"
                    f"{new_value}"
                    f"{match.group(3)}"
                )

            new_content = pattern.sub(
                replace_value,
                new_content,
            )

        if new_content == content:
            return True

        with open(main_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        return True