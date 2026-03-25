from gen.services import create_react_project_service


## Para ejecutar este test, ejecuta el script con Python 3:
## -> python3 test_react.py

print("ANTES")

result = create_react_project_service(
    project_name="demo-react",
    project_path="/tmp"
)

print("DESPUÉS")
print(result)

