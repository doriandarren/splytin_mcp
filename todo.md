# TODOs


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
from apps.ai_text_generation_prompts.api.views import AiTextGenerationPromptApiViewSet

# example
router_ai_text_generation_prompt = DefaultRouter()

# examples
router_ai_text_generation_prompt.register(
    prefix='ai_text_generation_prompts',
    basename='ai_text_generation_prompts',
    viewset=AiTextGenerationPromptApiViewSet
)


serializers.py:

from rest_framework.serializers import ModelSerializer
from apps.ai_text_generation_prompts.models import AiTextGenerationPrompt


class aiTextGenerationPromptSerializer(ModelSerializer):

    class Meta:
        model = AiTextGenerationPrompt
        ## fields = "__all__"
        fields = ['id', 'system_role','system_message','user_role','user_message','is_processed']

views.py:

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.ai_text_generation_prompts.api.serializers import AiTextGenerationPromptSerializer
from apps.ai_text_generation_prompts.models import AiTextGenerationPrompt


class AiTextGenerationPromptApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AiTextGenerationPromptSerializer
    queryset = AiTextGenerationPrompt.objects.all()

```


