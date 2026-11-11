import os
from gen.helpers.helper_file import HelperFile



class DjSeedAll:

    def invoke(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "main", "management", "commands")

        content = r'''from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Ejecuta todos los seeders del proyecto"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=10,
            help="Cantidad de registros por seeder"
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]

        if count < 1:
            raise CommandError("El número de registros debe ser mayor que cero.")

        # Seeders
        call_command("seed_users")
        call_command("seed_countries")
        call_command("seed_systems", count=count)
        call_command("seed_quotes", count=count)
        call_command("seed_teams", count=count)
        
        #call_command("seed_ai_prompt_categories", count=count)
        #call_command("seed_ai_prompt_generations", count=count)

        self.stdout.write(
            self.style.SUCCESS(
                "Todos los seeders ejecutados correctamente.
            ")
        )
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="seed_all.py",
            content=content
        )