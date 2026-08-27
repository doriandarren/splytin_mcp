from gen.php_laravel.to_create_project.auth.generate_auth_forgot_password import generate_auth_forgot_password
from gen.php_laravel.to_create_project.auth.generate_auth_login import generate_auth_login
from gen.php_laravel.to_create_project.auth.generate_auth_logout import generate_auth_logout
from gen.php_laravel.to_create_project.auth.generate_auth_register import generate_auth_register
from gen.php_laravel.to_create_project.auth.generate_auth_reset_password import generate_auth_reset_password
from gen.php_laravel.to_create_project.auth.generate_auth_route import generate_auth_route
from gen.php_laravel.to_create_project.auth.generate_auth_user import generate_auth_user



def generate_module_auth(full_path):
    # Login
    generate_auth_login(full_path)
    
    # Logout
    generate_auth_logout(full_path)
    
    # Register
    generate_auth_register(full_path)
    
    # Forgot Password
    generate_auth_forgot_password(full_path)
    
    # Restore Password
    generate_auth_reset_password(full_path)
    
    # Auth User 
    generate_auth_user(full_path)
    
    # Route
    generate_auth_route(full_path)
    
    