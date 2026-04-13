# Pendintes:


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
















# Risk - Globaltank

[risk_methods] RiskMethod *** RiskMethods : name
[risk_datatables] RiskDatatable *** RiskDatatables : customer_id customer_code company_name active_provisional type service_id service_name balance limit remaining_percentage
[risk_transactions] RiskTransaction *** RiskTransactions : movement_date movement_type service_id customer_id description table_origin record_id sign amount type deadline paid provisional_source
[risk_request_agent_status] RiskRequestAgentStatus *** RiskRequestAgentStatuses : name_es name_en name_ca
[risk_services] RiskService *** RiskServices : name status
[risk_customer_status] RiskCustomerStatus *** RiskCustomerStatuses : customer_id status_id
[risk_request_agent_companies] RiskRequestAgentCompany *** RiskRequestAgentCompanies : service_id methods_id authorizers_id risk_company_id risk_granted risk_award cod_debtor
[risk_request_agent_update_files] RiskRequestAgentUpdateFile *** RiskRequestAgentUpdateFiles : order_id service_id name_file type_file url
[customer_risk] CustomerRisk *** CustomerRisks : customer_id user_id company_id contract_company_id service_id risk_by_company risk_by_customer debtor_code obtained_risk obtained_method obtained_date granted_risk granted_date expiration_date visa_payment cancelled
[risk_companies] RiskCompany *** RiskCompanies : name address phone
[risk_customer_types] RiskCustomerType *** RiskCustomerTypes : customer_id type_id service_id
[risk_request_agent_services] RiskRequestAgentService *** RiskRequestAgentServices : req_risk_id service_id type_order month_cons risk_req units status_id service_location
[risk_provisional] RiskProvisional *** RiskProvisionals : authorizer_id service_id user_id amount customer_id used_amount status paid due_date
[risk_alerts] RiskAlert *** RiskAlerts : customer_id first second third service_id
[risk_request_agent_mail] RiskRequestAgentMail *** RiskRequestAgentMails : service_id link expiration_date_link status
[risk_monitor_transactions_copy_200924] RiskMonitorTransactionsCopy200924 *** RiskMonitorTransactionsCopy200924s : movement_date movement_type service_id customer_id in out balance description table_origin country provider_id record_id type deadline paid gt_risk_confirmed
[risk_company_services] RiskCompanyService *** RiskCompanyServices : company_id service_id
[risk_status] RiskStatus *** RiskStatuses : name
[risk_movement_types] RiskMovementType *** RiskMovementTypes : type_name service_id database_connection table_name where_field where_value movement_date_format has_vat vat_rate group_res in_select
[risk_request_agent] RiskRequestAgent *** RiskRequestAgents : agent_id customer_code order_string serie order_nb name email type dni_cif address zip_code city state country_id country_name name_admin surnames_admin dni_admin phone_admin observations
[risk_authorizers] RiskAuthorizer *** RiskAuthorizers : name
[contract_companies] ContractCompany *** ContractCompanies : name company_id serial internal_serial customer_id
[risk_monitor_transactions] RiskMonitorTransaction *** RiskMonitorTransactions : movement_date movement_type service_id customer_id in out balance description table_origin country provider_id record_id type deadline paid gt_risk_confirmed
[risk_types] RiskType *** RiskTypes : name
[risk_blocked] RiskBlocked *** RiskBlockeds : customer_id service_id
[risk_transaction_field_conversions] RiskTransactionFieldConversion *** RiskTransactionFieldConversions : name axxes_tolle_files telepass_elcon_headers ingenico_mvgl_files ingenico_dual_mvgl_files tokheim_xml_movements_tmp parking_movements
[risk_comments] RiskComment *** RiskComments : customer_id service_id comment
[risk_customer_notification_emails] RiskCustomerNotificationEmail *** RiskCustomerNotificationEmails : customer_id service_id email


