# TODOs

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


