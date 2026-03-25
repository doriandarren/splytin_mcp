from gen.services import create_php_project_service

# Para ejecutar este test, ejecuta el script con Python 3:
# -> python3 test_php.py

print("ANTES")

result = create_php_project_service(
    project_name="demo-php",
    project_path="/tmp"
)

print("DESPUÉS")
print(result)