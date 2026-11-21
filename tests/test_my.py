import os

from dotenv import load_dotenv
from gen.php_laravel.to_create_project.scripts.laravel_postman import LaravelPostman
from helpers.helper_string import normalize_project_name


load_dotenv()


"""
    Importante: 
    
    Para ejecutar:
    # python -m tests.test_my

"""
def invoke():
    full_path = "/Users/dorian/PHPProjects/api.app1.com"
    project_name = normalize_project_name("api.app1.com")
    domain_name = "app1.com"
    
    password = os.getenv("PASSWORD", "")
    
    obj = LaravelPostman()
    obj.invoke(full_path, project_name, domain_name, password)








if __name__ == '__main__':
    invoke()