from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from gen.services import create_php_project_service

# Para ejecutar este test, ejecuta el script con Python 3:
# -> python3 tests/test_php.py

print("ANTES")

result = create_php_project_service(
    project_name="demo-php",
    project_path="/tmp"
)

print("DESPUÉS")
print(result)
