
import os
from gen.helpers.helper_file import HelperFile


class ReactTsCrudCreate:

    @staticmethod
    def get_default_value(column):
        """
        Genera el valor inicial de una columna.
        """

        column_type = column.get("type", "string")

        if column.get("is_nullable", False):
            return "null"

        if column_type == "boolean":
            return "false"

        if column_type in (
            "integer", "int", "bigint", "smallint",
            "decimal", "float", "double", "fk"
        ) or column.get("is_fk", False):
            return "0"

        return '""'

    @staticmethod
    def generate_form_initial_values(columns):
        """
        Genera los valores iniciales del formulario.
        """

        result = []

        excluded = {"id", "created_at", "updated_at"}

        for column in columns:
            name = column["name"]

            if name in excluded:
                continue

            default_value = ReactTsCrudCreate.get_default_value(
                column
            )

            result.append(
                f"    {name}: {default_value},"
            )

        return "\n".join(result)

    @staticmethod
    def generate_form_field(column):
        """
        Genera un campo JSX según su tipo.
        """

        name = column["name"]
        column_type = column.get("type", "string")
        is_nullable = column.get("is_nullable", False)
        is_unsigned = column.get("is_unsigned", False)
        size = column.get("size")

        required = "" if is_nullable else "\n              required"

        # Boolean
        if column_type == "boolean":
            return f'''          {{/* {name} */}}
          <div className="space-y-2">
            <Label htmlFor="{name}">{name}</Label>
            <Input
              id="{name}"
              type="checkbox"
              checked={{form.{name} ?? false}}
              onChange={{(event) =>
                setForm((prev) => ({{
                  ...prev,
                  {name}: event.target.checked,
                }}))
              }}
              className="size-4"
            />
          </div>'''

        # Campos numéricos
        if column_type in (
            "integer", "int", "bigint", "smallint",
            "decimal", "float", "double", "fk"
        ) or column.get("is_fk", False):

            step = (
                "any"
                if column_type in ("decimal", "float", "double")
                else "1"
            )

            min_attribute = (
                '\n              min="0"'
                if is_unsigned
                else ""
            )

            if is_nullable:
                value_expression = (
                    'event.target.value === "" '
                    '? null : Number(event.target.value)'
                )
            else:
                value_expression = (
                    'Number(event.target.value)'
                )

            return f'''          {{/* {name} */}}
          <div className="space-y-2">
            <Label htmlFor="{name}">{name}</Label>
            <Input
              id="{name}"
              type="number"
              step="{step}"{min_attribute}
              value={{form.{name} ?? ""}}
              onChange={{(event) =>
                setForm((prev) => ({{
                  ...prev,
                  {name}: {value_expression},
                }}))
              }}{required}
            />
          </div>'''

        # Campos de texto
        input_type = "text"

        if column_type == "date":
            input_type = "date"

        elif column_type in ("datetime", "timestamp"):
            input_type = "text"

        elif column_type == "time":
            input_type = "time"

        max_length = ""

        if size is not None and column_type == "string":
            max_length = f'\n              maxLength={{{size}}}'

        if is_nullable:
            value_expression = (
                'event.target.value === "" '
                '? null : event.target.value'
            )
        else:
            value_expression = "event.target.value"

        return f'''          {{/* {name} */}}
          <div className="space-y-2">
            <Label htmlFor="{name}">{name}</Label>
            <Input
              id="{name}"
              type="{input_type}"
              value={{form.{name} ?? ""}}
              onChange={{(event) =>
                setForm((prev) => ({{
                  ...prev,
                  {name}: {value_expression},
                }}))
              }}{max_length}{required}
            />
          </div>'''

    @staticmethod
    def generate_form_fields(columns):
        """
        Genera todos los campos JSX
        a partir de columns.
        """

        result = []

        excluded = {"id", "created_at", "updated_at"}

        for column in columns:
            if column["name"] in excluded:
                continue

            result.append(
                ReactTsCrudCreate.generate_form_field(column)
            )

        return "\n\n".join(result)




    def invoke(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    ):
        """
        Genera los archivos de creación CRUD.
        """

        self.create_file_page(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        
        
        self.create_file_hook(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        
        
        
        

    def create_file_page(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    ):
        """
        Genera la página Create React + TypeScript.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "pages"
        )

        component_name = f"{singular_name}CreatePage"
        hook_name = f"useCreate{singular_name}"
        input_name = f"Create{singular_name}Input"

        route_path = f"/admin/{plural_name_kebab}"

        initial_values = self.generate_form_initial_values(
            columns
        )

        form_fields = self.generate_form_fields(columns)

        content = f'''// src/modules/{namespace}/{plural_name_snake}/pages/{component_name}.tsx

import {{ useState }} from "react";
import {{ useNavigate }} from "react-router";
import {{ ArrowLeft, Save }} from "lucide-react";

import {{ Button }} from "@/components/ui/button";
import {{ Input }} from "@/components/ui/input";
import {{ Label }} from "@/components/ui/label";

import {{ {hook_name} }} from "../hooks/{hook_name}";
import type {{ {input_name} }} from "../types/{singular_name_snake}.types";

export const {component_name} = () => {{
  const navigate = useNavigate();
  const createItem = {hook_name}();

  const [form, setForm] = useState<{input_name}>({{
{initial_values}
  }});

  const handleSubmit = async (
    event: React.SubmitEvent<HTMLFormElement>
  ) => {{
    event.preventDefault();

    try {{
      await createItem.mutateAsync(form);

      navigate("{route_path}");
    }} catch {{
      // El error se muestra debajo del formulario.
    }}
  }};

  return (
    <div className="space-y-6 p-6">
      {{/* Cabecera */}}
      <div>
        <Button
          variant="ghost"
          onClick={{() => navigate("{route_path}")}}
        >
          <ArrowLeft className="size-4" />
          Volver
        </Button>

        <h1 className="mt-4 text-3xl font-bold">
          Crear {singular_name}
        </h1>

        <p className="text-sm text-muted-foreground">
          Introduce los datos del nuevo {singular_name}.
        </p>
      </div>

      {{/* Formulario */}}
      <form
        onSubmit={{handleSubmit}}
        className="space-y-6"
      >
        <div className="rounded-lg border bg-card p-6">
          <div className="grid gap-6 md:grid-cols-2">
{form_fields}
          </div>
        </div>

        {{/* Error */}}
        {{createItem.isError && (
          <p role="alert" className="text-sm text-destructive">
            {{createItem.error.message}}
          </p>
        )}}

        {{/* Botones */}}
        <div className="flex justify-end gap-3">
          <Button
            type="button"
            variant="outline"
            onClick={{() => navigate("{route_path}")}}
            disabled={{createItem.isPending}}
          >
            Cancelar
          </Button>

          <Button
            type="submit"
            disabled={{createItem.isPending}}
          >
            <Save className="size-4" />
            {{createItem.isPending
              ? "Guardando..."
              : "Guardar"}}
          </Button>
        </div>
      </form>
    </div>
  );
}};
'''

        return HelperFile.write(
            folder_path=folder_path,
            file_name=f"{component_name}.tsx",
            content=content
        )





    def create_file_hook(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    ):
        """
    Genera el hook React Query para crear un recurso.
    """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "hooks"
        )

        content = f'''// src/modules/{namespace}/{plural_name_snake}/hooks/useCreate{singular_name}.ts
import {{ useMutation, useQueryClient }} from "@tanstack/react-query";

import {{ create{singular_name} }} from "../systems/{plural_name_camel}Service";
import {{ {plural_name_camel}Keys }} from "../queries/{plural_name_camel}Queries";

export const useCreate{singular_name} = () => {{
const queryClient = useQueryClient();

return useMutation({{
    mutationFn: create{singular_name},

    onSuccess: async () => {{
    await queryClient.invalidateQueries({{
        queryKey: {plural_name_camel}Keys.lists(),
    }});
    }},
}});
}};
'''

        return HelperFile.write(
            folder_path=folder_path,
            file_name=f"useCreate{singular_name}.ts",
            content=content
        )