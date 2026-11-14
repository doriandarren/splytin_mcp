from gen.php_laravel.to_create_project.utilities.excel.generate_excel import generate_excel
from gen.php_laravel.to_create_project.utilities.helpers.generate_helpers import generate_helpers
from gen.php_laravel.to_create_project.utilities.messages.laravel_messages import generate_messages



class LaravelUtilities:

    def invoke(self, full_path):
        generate_excel(full_path)
        generate_helpers(full_path)
        generate_messages(full_path)

