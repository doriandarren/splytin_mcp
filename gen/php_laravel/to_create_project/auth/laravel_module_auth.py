from gen.php_laravel.to_create_project.auth.laravel_auth_forgot_password import LaravelAuthForgotPassword
from gen.php_laravel.to_create_project.auth.laravel_auth_login import LaravelAuthLogin
from gen.php_laravel.to_create_project.auth.laravel_auth_logout import LaravelAuthLogout
from gen.php_laravel.to_create_project.auth.laravel_auth_register import LaravelAuthRegister
from gen.php_laravel.to_create_project.auth.laravel_auth_reset_password import LaravelAuthResetPassword
from gen.php_laravel.to_create_project.auth.laravel_auth_route import LaravelAuthRoute
from gen.php_laravel.to_create_project.auth.laravel_auth_user import LaravelAuthUser



class LaravelModuleAuth:

    def invoke(self, full_path):
        # Login
        obj = LaravelAuthLogin()
        obj.invoke(full_path)
        
        # Logout
        obj = LaravelAuthLogout()
        obj.invoke(full_path)
        
        # Register
        obj = LaravelAuthRegister()
        obj.invoke(full_path)
        
        # Forgot Password
        obj = LaravelAuthForgotPassword()
        obj.invoke(full_path)
        
        # Reset Password
        obj = LaravelAuthResetPassword()
        obj.invoke(full_path)
        
        # Auth User 
        obj = LaravelAuthUser()
        obj.invoke(full_path)
        
        # Route
        obj = LaravelAuthRoute()
        obj.invoke(full_path)
    
    