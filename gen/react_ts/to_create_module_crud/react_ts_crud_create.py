
import os

from helpers.helper_file import HelperFile
from gen.react_ts.helpers.helper_react_ts_create import HelperReactTsCreate
from gen.react_ts.helpers.helper_react_ts_zod_react_form import HelperReactTsZodReactForm


class ReactTsCrudCreate:

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
        
        self.create_zod_react_form(
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
        Genera la página Create React + TypeScript
        utilizando React Hook Form y Zod.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "pages"
        )

        content = f'''// src/modules/{namespace}/{plural_name_snake}/pages/{singular_name}CreatePage.tsx
import {{ useNavigate }} from "react-router";
import {{ ArrowLeft, Save }} from "lucide-react";
import {{ alerta }} from "@/components/alerts/alerta";
import {{ useForm }} from "react-hook-form";
import {{ zodResolver }} from "@hookform/resolvers/zod";
import {{ Button }} from "@/components/ui/button";
import {{ Input }} from "@/components/ui/input";
import {{ Label }} from "@/components/ui/label";
import {{ useCreate{singular_name} }} from "../hooks/useCreate{singular_name}";


import {{
  {singular_name_camel}Schema,
  type {singular_name}FormValues,
}} from "../schemas/{singular_name_camel}.schema";

export const {singular_name}CreatePage = () => {{
  const navigate = useNavigate();
  const createItem = useCreate{singular_name}();

  // Formulario y validación
  const {{
    register,
    handleSubmit,
    formState: {{ errors }},
  }} = useForm<{singular_name}FormValues>({{
    resolver: zodResolver({singular_name_camel}Schema),
    mode: "onTouched",
    defaultValues: {{
{HelperReactTsCreate.generate_form_initial_values(columns)}
    }},
  }});

  // Guardar registro
  const onSubmit = async (values: {singular_name}FormValues) => {{
    try {{
      await createItem.mutateAsync(values);
      alerta.success("Registro creado correctamente");
      navigate("/admin/{plural_name_kebab}");
    }} catch {{
      // El error se muestra en el formulario.
    }}
  }};

  return (
    <div className="space-y-6 p-6">
      {{/* Cabecera */}}
      <div>
        <Button
          variant="ghost"
          onClick={{() => navigate("/admin/{plural_name_kebab}")}}
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
        onSubmit={{handleSubmit(onSubmit)}}
        noValidate
        className="space-y-6"
      >
        <div className="rounded-lg border bg-card p-6">
          <h2 className="mb-6 text-lg font-semibold">
            Información general
          </h2>

          <div className="grid gap-6 md:grid-cols-2">
{HelperReactTsCreate.generate_form_fields(columns)}
          </div>
        </div>

        {{/* Error de la API */}}
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
            onClick={{() => navigate("/admin/{plural_name_kebab}")}}
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

        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}CreatePage.tsx",
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

import {{ create{singular_name} }} from "../services/{plural_name_camel}Service";
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

        HelperFile.write(
            folder_path=folder_path,
            file_name=f"useCreate{singular_name}.ts",
            content=content
        )



    def create_zod_react_form(
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
            Genera el archivo del esquema Zod.
            """
    
            folder_path = os.path.join(
                full_path,
                "src",
                "modules",
                namespace,
                plural_name_snake,
                "schemas"
            )
    
            content = f'''// src/modules/{namespace}/{plural_name_snake}/schemas/{singular_name_camel}.schema.ts    
import {{ z }} from "zod";

export const {singular_name_camel}Schema = z.object({{
{HelperReactTsZodReactForm.generate_schema_fields(columns)}
}});

export type {singular_name}FormValues = z.infer<
  typeof {singular_name_camel}Schema
>;
'''
    
            return HelperFile.write(
                folder_path=folder_path,
                file_name=f"{singular_name_camel}.schema.ts",
                content=content
            )
            
