import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import helper_append_content
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from gen.helpers.helper_print import print_message, GREEN, CYAN


def generate_module_devs(full_path, project_name_format, app_main):
    create_module_devs(full_path, project_name_format, app_main)
    update_file_api_views(full_path, project_name_format, app_main)
    
    ## Emails
    create_email_service(full_path, project_name_format, app_main)
    append_settings(full_path, app_main)
    create_email_html(full_path, project_name_format, app_main)



def create_module_devs(full_path, project_name_format, app_main):
    """
    Crea el modulo
    """
    print_message(f"Generando el modulo de Users", CYAN)
    singular_name = "Dev"
    plural_name = "Devs"
    columns = "test"
    input_menu_checkbox = ['api_route', 'api_serializer', 'api_wiewset']
    formatColumns = parse_columns_input(columns)
    
    standard_module_crud_python_django(full_path, app_main, singular_name, plural_name, formatColumns, input_menu_checkbox)
    


def update_file_api_views(full_path, project_name_format, app_main):
    """
    Actualiza el archivo
    """
    folder_path = os.path.join(full_path, "apps", "devs", "api")
    file_path = os.path.join(folder_path, "views.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action


class DevApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, methods=['get'], url_path='test')
    def invoke(self, request):
        try:
            
            response = {
                "message": "OK"
            }
            return Response({
                'message': response,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    
    @action(detail=False, methods=['get'], url_path='test_email')
    def invoke_email(self, request):
        """ Envio de correo de prueba."""
        try:
            
            mail_service = SendMailService(
                subject="Correo Prueba",
                to_emails=["doriandarren1@gmail.com"],
            )
            
            mail_service.send_html_mail(
                title="Correo de prueba",
                body="Hola,\n\nEste es un correo de prueba.\n\nGracias por tu tiempo."
            )
            
            
            response = {
                "message": "OK"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)









def create_email_service(full_path, project_name_format, app_main):
    """
    Actualiza el archivo
    """
    folder_path = os.path.join(full_path, "apps", "devs", "services")
    file_path = os.path.join(folder_path, "send_email_service.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class SendMailService:

    def __init__(self, subject, to_emails, from_email=None):
        self.subject = subject
        self.to_emails = [to_emails] if isinstance(to_emails, str) else to_emails
        self.from_email = from_email or settings.DEFAULT_FROM_EMAIL
        self.template_html = "emails/test_email.html"

    def send_html_mail(self, title, body):
        html_content = render_to_string(self.template_html, {
            "title": title,
            "body": body,
        })

        msg = EmailMultiAlternatives(
            subject=self.subject,
            body="",
            from_email=self.from_email,
            to=self.to_emails,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return True
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)




    
def append_settings(full_path, app_main):    
    
    str = r"""# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.ionos.es"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "webmaster@splytin.com"
EMAIL_HOST_PASSWORD = "D1l@an-2013"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    """
    
    helper_append_content(
        full_path, 
        f"{app_main}/settings.py", 
        str
    )
    
   
   
def create_email_html(full_path, project_name_format, app_main):
    """
    Actualiza el archivo
    """
    folder_path = os.path.join(full_path, "templates", "emails")
    file_path = os.path.join(folder_path, "test_email.html")

    os.makedirs(folder_path, exist_ok=True)
    
    project_name_upper = project_name_format.toUpperCase().replace(" ", "_")

    content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body style="margin:0; padding:0; background-color:#f4f6f9; font-family:Arial, Helvetica, sans-serif; color:#333333;">

    <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f6f9; margin:0; padding:30px 0;">
        <tr>
            <td align="center">

                <table width="650" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 4px 14px rgba(0,0,0,0.08);">

                    <!-- HEADER -->
                    <tr>
                        <td style="background:linear-gradient(135deg, #0f172a, #1e293b); padding:30px; text-align:center;">
                            <h1 style="margin:0; color:#ffffff; font-size:28px; font-weight:bold;">
                                {project_name_upper}
                            </h1>
                            <p style="margin:8px 0 0 0; color:#cbd5e1; font-size:14px;">
                                Comunicación automática
                            </p>
                        </td>
                    </tr>

                    <!-- CONTENIDO -->
                    <tr>
                        <td style="padding:35px 40px 20px 40px;">
                            <h2 style="margin:0 0 20px 0; color:#111827; font-size:24px; text-align:center;">
                                {{{{ title }}}}
                            </h2>

                            <div style="font-size:15px; line-height:1.8; color:#374151;">
                                {{{{ body|linebreaks }}}}
                            </div>
                        </td>
                    </tr>

                    <!-- BLOQUE SUAVE -->
                    <tr>
                        <td style="padding:10px 40px 35px 40px;">
                            <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f9fafb; border:1px solid #e5e7eb; border-radius:10px;">
                                <tr>
                                    <td style="padding:20px; text-align:center;">
                                        <p style="margin:0; font-size:13px; color:#6b7280;">
                                            Gracias por confiar en <strong>{project_name_upper}</strong>.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- FOOTER -->
                    <tr>
                        <td style="padding:30px 40px; background-color:#fafafa; border-top:1px solid #e5e7eb;">

                            <p style="font-size:10px; text-align:justify; color:#6b7280; line-height:1.6; margin:0 0 14px 0;">
                                <strong>AVISO LEGAL:</strong> Este mensaje y sus posibles documentos adjuntos son confidenciales y están
                                dirigidos exclusivamente a sus destinatarios. Por favor, si Ud. no es uno de ellos, notifíquenoslo y
                                elimine el mensaje de su sistema. De conformidad con la legislación vigente, queda prohibida la copia,
                                difusión o revelación de su contenido a terceros sin el previo consentimiento por escrito de {project_name_upper}.
                                Asimismo, en relación con la normativa de protección de datos puede ejercer sus derechos de acceso,
                                rectificación, cancelación, oposición y portabilidad de acuerdo a lo establecido en nuestra política
                                de privacidad en la siguiente dirección: Avda. Europa 26, 17469 Vilamalla (Girona), España.
                            </p>

                            <p style="font-size:10px; text-align:justify; color:#6b7280; line-height:1.6; margin:0 0 16px 0;">
                                <strong>LEGAL NOTICE:</strong> This message (including any attachments) may contain privileged and/or
                                confidential information. Therefore, we would like to inform whoever may receive it by mistake that the
                                information contained herein is strictly confidential, and its unauthorized use is prohibited by law.
                                Therefore, in this case, please notify us by email and refrain from copying the message or forwarding
                                it to third parties, and proceed to delete it immediately. According to applicable data protection
                                regulations, {project_name_upper} informs you that your data is protected under current legislation. The owner of
                                the data will have, at any time, the right to access the files, and can also exercise the rights of
                                rectification, cancellation and opposition in the terms included in the data protection legislation at
                                the following address: Avda. Europa 26, 17469 Vilamalla (Girona), España.
                            </p>

                            <hr style="margin:18px 0; border:none; border-top:1px solid #d1d5db;">

                            <p style="font-size:12px; color:#9ca3af; text-align:center; margin:0;">
                                &copy; {{% now "Y" %}} {project_name_upper}. All rights reserved.
                            </p>

                        </td>
                    </tr>

                </table>

            </td>
        </tr>
    </table>

</body>
</html>
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)