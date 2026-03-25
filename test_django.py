from gen.services import create_python_django_project_service

# Para ejecutar 
# python3 test_django.py

print("ANTES")

result = create_python_django_project_service(
    project_name="demo-django",
    project_path="/tmp",
    app_name="main"
)

print("DESPUÉS")
print(result)