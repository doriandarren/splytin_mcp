from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from gen.services import create_react_project_service


## Para ejecutar este test, ejecuta el script con Python 3:
## -> python3 tests/test_react.py

print("ANTES")

result = create_react_project_service(
    project_name="demo-react",
    project_path="/tmp"
)

print("DESPUÉS")
print(result)
