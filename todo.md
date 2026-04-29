# Pendintes:


- Python django: agregar logica de users esta creado en el proyecto de: python.splytin.com ...IMPORTANTE...

- En php: crear y modificar en vez de repositorio por service



# Project

```sh

barriles de maderas
barriles de aceros (gasolina)


Lista de objetos:

cajas de madera
cajas rotas
mesas
sillas
bancos
estanterías
armarios
puertas viejas apoyadas

faroles
velas
botellas
libros
platos
jarras
sacos
cubos

árboles
troncos cortados
rocas
vallas de madera
postes
señales

lámparas
faroles colgantes
antorchas
interruptores (opcional)
cables



```

# Kotlin

```sh

- hacer strings.xml

- Edita gradle/libs.versions.toml:

[versions]
navigationCompose = "2.9.7"

[libraries]
androidx-navigation-compose = { group = "androidx.navigation", name = "navigation-compose", version.ref = "navigationCompose" }
androidx-compose-material-icons-extended = { group = "androidx.compose.material", name = "material-icons-extended" }
androidx-compose-material = { group = "androidx.compose.material", name = "material" }



- Edita: app/build.gradle.kts:

dependencies:
implementation(libs.androidx.navigation.compose)
implementation(libs.androidx.compose.material)
implementation("com.squareup.retrofit2:retrofit:2.11.0")
implementation("com.squareup.retrofit2:converter-gson:2.11.0")



- Editar el AndroidManifest.xml:

<uses-permission android:name="android.permission.INTERNET" />





- Modificar MainActivity.kt
- Agregar AppNavigation.kt




- crear Core:

com.www.testgeneratorandroid.core.network
-> RetrofitClient.kt


- Modulo Auth:

com.www.testgeneratorandroid.modules.auth.models
-> LoginRequest.kt
-> LoginResponse.kt
-> AuthResponse.kt

com.www.testgeneratorandroid.modules.auth.repositories
-> AuthRepository.kt

com.www.testgeneratorandroid.modules.auth.screens
-> LoginScreen.kt

com.www.testgeneratorandroid.modules.auth.services
-> AuthApiService.kt







com.www.testgeneratorandroid.ui.screens -> Agregar HomeScreen.kt y Agregar LoginScreen.kt


com.www.testgeneratorandroid.data.models
com.www.testgeneratorandroid.data.network
com.www.testgeneratorandroid.data.repositories








```

## Prompt

```sh

Para que entiendas el conexto que necesito. Tengo una carpeta en la raíz del proyecto por ejemplo: apps/AiTextGenerationPrompt/api. Con estas carpetas: router.py, serializers.py y views.py

router.py:

from rest_framework.routers import DefaultRouter
from apps.ai_prompt_categories.api.views import AiPromptCategoryApiViewSet

# example
router_ai_prompt_category = DefaultRouter()

# examples
router_ai_prompt_category.register(
    prefix='ai_prompt_categories',
    basename='ai_prompt_categories',
    viewset=AiPromptCategoryApiViewSet
)

serializers.py:

from rest_framework.serializers import ModelSerializer
from apps.ai_prompt_categories.models import AiPromptCategory

class AiPromptCategorySerializer(ModelSerializer):
    class Meta:
        model = AiPromptCategory
        ## fields = "__all__"
        fields = [
            'id',
            'name',
            'description',
            'slug',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]

views.py:

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.ai_prompt_categories.api.serializers import AiPromptCategorySerializer
from apps.ai_prompt_categories.models import AiPromptCategory

class AiPromptCategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AiPromptCategorySerializer
    queryset = AiPromptCategory.objects.all()

```


