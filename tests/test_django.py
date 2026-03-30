from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from gen.services import create_python_django_project_service

# Para ejecutar 
# python3 tests/test_django.py

print("ANTES")

result = create_python_django_project_service(
    project_name="demo-django",
    project_path="/tmp",
    app_main="main"
)

print("DESPUÉS")
print(result)
