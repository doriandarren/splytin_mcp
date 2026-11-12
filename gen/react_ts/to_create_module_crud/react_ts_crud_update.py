
import os

from helpers.helper_file import HelperFile
from gen.react_ts.helpers.helper_react_ts_create import HelperReactTsCreate


class ReactTsCrudUpdate:

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
        Genera los archivos de actualización CRUD.
        """

        self.create_hook_use_ts(
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

        self.create_hook_use_update_ts(
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

        self.create_system_update_page_tsx(
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




    def create_hook_use_ts(
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
        Genera el hook para consultar un recurso por ID.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "hooks"
        )

        content = f'''// src/modules/{namespace}/{plural_name_snake}/hooks/use{singular_name}.ts

import {{ useQuery }} from "@tanstack/react-query";

import {{ get{singular_name} }} from "../services/{plural_name_camel}Service";

export const use{singular_name} = (id: string | undefined) => {{
  return useQuery({{
    queryKey: ["{plural_name_camel}", "detail", id],

    queryFn: ({{ signal }}) => {{
      if (!id) {{
        throw new Error("ID de {singular_name} no válido.");
      }}

      return get{singular_name}(id, signal);
    }},

    enabled: Boolean(id),
  }});
}};
'''

        HelperFile.write(
            folder_path=folder_path,
            file_name=f"use{singular_name}.ts",
            content=content
        )




    def create_hook_use_update_ts(
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
        Genera el hook para actualizar un recurso.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "hooks"
        )

        content = f'''// src/modules/{namespace}/{plural_name_snake}/hooks/useUpdate{singular_name}.ts

import {{ useMutation, useQueryClient }} from "@tanstack/react-query";

import {{ update{singular_name} }} from "../services/{plural_name_camel}Service";
import {{ {plural_name_camel}Keys }} from "../queries/{plural_name_camel}Queries";

import type {{ Update{singular_name}Input }} from "../types/{singular_name_snake}.types";

interface Update{singular_name}Params {{
  id: string;
  input: Update{singular_name}Input;
}}

export const useUpdate{singular_name} = () => {{
  const queryClient = useQueryClient();

  return useMutation({{
    mutationFn: ({{ id, input }}: Update{singular_name}Params) =>
      update{singular_name}(id, input),

    onSuccess: async (_data, variables) => {{
      await Promise.all([
        queryClient.invalidateQueries({{
          queryKey: {plural_name_camel}Keys.lists(),
        }}),

        queryClient.invalidateQueries({{
          queryKey: ["{plural_name_camel}", "detail", variables.id],
        }}),
      ]);
    }},
  }});
}};
'''

        HelperFile.write(
            folder_path=folder_path,
            file_name=f"useUpdate{singular_name}.ts",
            content=content
        )




    def create_system_update_page_tsx(
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
        Genera la página Update utilizando
        React Hook Form y Zod.
        """

        folder_path = os.path.join(
            full_path,
            "src",
            "modules",
            namespace,
            plural_name_snake,
            "pages"
        )

        content = f'''// src/modules/{namespace}/{plural_name_snake}/pages/{singular_name}UpdatePage.tsx

import {{ useEffect }} from "react";
import {{ useNavigate, useParams }} from "react-router";
import {{ ArrowLeft, Save }} from "lucide-react";
import {{ alerta }} from "@/components/alerts/alerta";
import {{ useForm }} from "react-hook-form";
import {{ zodResolver }} from "@hookform/resolvers/zod";
import {{ Button }} from "@/components/ui/button";
import {{ Input }} from "@/components/ui/input";
import {{ Label }} from "@/components/ui/label";
import {{ use{singular_name} }} from "../hooks/use{singular_name}";
import {{ useUpdate{singular_name} }} from "../hooks/useUpdate{singular_name}";
import {{
  {singular_name_camel}Schema,
  type {singular_name}FormValues,
}} from "../schemas/{singular_name_camel}.schema";



export const {singular_name}UpdatePage = () => {{
  const navigate = useNavigate();
  const {{ id }} = useParams<{{ id: string }}>();

  const query = use{singular_name}(id);
  const updateItem = useUpdate{singular_name}();

  // Formulario y validación
  const {{
    register,
    handleSubmit,
    reset,
    formState: {{ errors }},
  }} = useForm<{singular_name}FormValues>({{
    resolver: zodResolver({singular_name_camel}Schema),
    mode: "onTouched",
    defaultValues: {{
{HelperReactTsCreate.generate_form_initial_values(columns)}
    }},
  }});

  // Cargar los datos actuales
  useEffect(() => {{
    if (query.data) {{
      reset(query.data.attributes);
    }}
  }}, [query.data, reset]);

  // Guardar cambios
  const onSubmit = async (values: {singular_name}FormValues) => {{
    if (!id) return;

    try {{
      await updateItem.mutateAsync({{
        id,
        input: values,
      }});

      alerta.success("Registro actualizado correctamente");
      navigate("/admin/{plural_name_kebab}");
    }} catch {{
      // El error se muestra en el formulario.
    }}
  }};

  // ID no válido
  if (!id) {{
    return (
      <div className="space-y-4 p-6">
        <p className="text-destructive">
          ID no válido.
        </p>
      </div>
    );
  }}

  // Cargando datos
  if (query.isPending) {{
    return (
      <div className="p-6">
        Cargando {singular_name}...
      </div>
    );
  }}

  // Error al consultar
  if (query.isError || !query.data) {{
    return (
      <div className="space-y-4 p-6">
        <p className="text-destructive">
          No se pudo cargar el registro.
        </p>

        <Button onClick={{() => void query.refetch()}}>
          Reintentar
        </Button>
      </div>
    );
  }}

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
          Editar {singular_name}
        </h1>

        <p className="text-sm text-muted-foreground">
          Modifica los datos del registro.
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
        {{updateItem.isError && (
          <p role="alert" className="text-sm text-destructive">
            {{updateItem.error.message}}
          </p>
        )}}

        {{/* Botones */}}
        <div className="flex justify-end gap-3">
          <Button
            type="button"
            variant="outline"
            onClick={{() => navigate("/admin/{plural_name_kebab}")}}
            disabled={{updateItem.isPending}}
          >
            Cancelar
          </Button>

          <Button
            type="submit"
            disabled={{updateItem.isPending}}
          >
            <Save className="size-4" />
            {{updateItem.isPending
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
            file_name=f"{singular_name}UpdatePage.tsx",
            content=content
        )
