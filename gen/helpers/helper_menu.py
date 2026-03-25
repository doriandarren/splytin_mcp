import os
try:
    import questionary
except ModuleNotFoundError:
    questionary = None
from gen.helpers.helper_print import print_header


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# def menu_list(msg, choices):

#     str_input = questionary.select(
#         msg,
#         choices=choices,
#         use_indicator=True
#     ).ask()

#     return str_input


def menu_list(msg, choices):
    """
    choices puede ser:
      - list[str]  -> devuelve str
      - list[dict] -> [{ "name": "...", "value": "..." }, ...] -> devuelve value
      - list[tuple] -> [("Label", "value"), ...] -> devuelve value
    """

    if questionary is None:
        print(msg)
        normalized_choices = []
        for c in choices:
            if isinstance(c, str):
                normalized_choices.append((c, c))
            elif isinstance(c, dict):
                normalized_choices.append((c["name"], c["value"]))
            elif isinstance(c, (tuple, list)) and len(c) == 2:
                normalized_choices.append((c[0], c[1]))
            else:
                raise TypeError(f"Formato de choice no soportado: {c!r}")

        for index, (label, _) in enumerate(normalized_choices, start=1):
            print(f"{index}. {label}")

        selected = input("Selecciona una opción: ").strip()
        return normalized_choices[int(selected) - 1][1]

    q_choices = []

    for c in choices:
        # Caso 1: "PHP", "React", ...
        if isinstance(c, str):
            q_choices.append(c)

        # Caso 2: {"name": "...", "value": "..."} (estilo Node)
        elif isinstance(c, dict):
            q_choices.append(questionary.Choice(title=c["name"], value=c["value"]))

        # Caso 3: ("Label", "value")
        elif isinstance(c, (tuple, list)) and len(c) == 2:
            label, value = c
            q_choices.append(questionary.Choice(title=label, value=value))

        else:
            raise TypeError(f"Formato de choice no soportado: {c!r}")

    return questionary.select(
        msg,
        choices=q_choices,
        use_indicator=True
    ).ask()



def pause():
    print("\n")
    if questionary is None:
        input("Presione ENTER para continuar ")
        return

    questionary.text("Presione ENTER para continuar ").ask()



def menu_checkbox(msg, choices_dict):
    if questionary is None:
        print(msg)
        return [value for _, value in choices_dict]

    choices = [
        questionary.Choice(title=label, value=value, checked=True)
        for label, value in choices_dict
    ]
    return questionary.checkbox(msg, choices=choices).ask()

