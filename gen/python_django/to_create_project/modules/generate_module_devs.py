import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.helpers.helper_file import helper_append_content, helper_create_init_file
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command


def generate_module_devs(full_path, project_name_format, app_main, venv_python):
    create_module_devs(full_path, project_name_format, app_main)
    update_file_api_views(full_path, project_name_format, app_main)
    
    ## Emails
    create_email_service(full_path, project_name_format, app_main)
    append_email_settings(full_path, project_name_format, app_main)
    create_email_html(full_path, project_name_format, app_main)


    # PDF
    install_pdf(full_path, venv_python)
    create_pdf_service(full_path, project_name_format, app_main)
    create_pdf_html(full_path, project_name_format, app_main)
    



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

    content = r'''from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

from apps.devs.services.email_service import MailService
from apps.devs.services.pdf_service import PdfService

class DevApiViewSet(ViewSet):
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
        """ EMAIL TEST 
            Envio de correo de prueba
        """
        try:
            
            mail_service = MailService(
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
    
    @action(detail=False, methods=['get'], url_path='test_pdf')
    def invoke_pdf(self, request):
        """ 
            Generación de PDF de prueba.
        """
        
        try:
            
            ## - Generar PDF y descargarlo
            
            # pdf_service = PdfService()
            # pdf_bytes = pdf_service.generate_pdf({
            #     "title": "PDF de prueba",
            #     "body": "Hola, este es un PDF generado desde Django con wkhtmltopdf.",
            # })
            # response = HttpResponse(pdf_bytes, content_type="application/pdf")
            # response["Content-Disposition"] = 'attachment; filename="prueba.pdf"'
            # return response
        
        
            ## - Guardar PDF en carpeta uploads/pdfs
            
            pdf_service = PdfService(
                template_html="pdfs/test_pdf.html"
            )

            file_path = pdf_service.save(
                filename="prueba.pdf",
                context={
                    "title": "PDF guardado",
                    "body": "Hola, este PDF se ha guardado en la carpeta uploads/pdfs.",
                }
            )
            
            response = {
                "message": "PDF generado y guardado correctamente",
                "file_path": file_path,
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



## Email service
def create_email_service(full_path, project_name_format, app_main):
    """
    Actualiza el archivo
    """
    folder_path = os.path.join(full_path, "apps", "devs", "services")
    file_path = os.path.join(folder_path, "email_service.py")

    os.makedirs(folder_path, exist_ok=True)
    
    helper_create_init_file(folder_path)

    content = r'''from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class MailService:

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

    
def append_email_settings(full_path, project_name_format, app_main):    
    
    str = f"""\n# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.ionos.es")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "False") == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
EMAIL_TIMEOUT = int(os.getenv("EMAIL_TIMEOUT", 30))
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
    
    project_name_upper = project_name_format.replace(" ", "_").upper()

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
        
        

  
## PDF service 

def install_pdf(full_path, venv_python):
    print_message("Instalando pdfkit...", CYAN)
    run_command(f'"{venv_python}" -m pip install pdfkit', cwd=full_path)
    print_message("pdfkit instalado correctamente.", GREEN)



def create_pdf_service(full_path, project_name_format, app_main):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "devs", "services")
    file_path = os.path.join(folder_path, "pdf_service.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''import os
import pdfkit

from django.conf import settings
from django.template.loader import render_to_string


class PdfService:

    def __init__(
        self,
        template_html="pdfs/test_pdf.html",
        wkhtmltopdf_path=None,
        footer_text="EMPRESA",
    ):
        self.template_html = template_html
        self.footer_text = footer_text
        self.app_env = getattr(settings, "APP_ENV", "local")
        self.wkhtmltopdf_path = wkhtmltopdf_path or self._detect_wkhtmltopdf_path()

    def _detect_wkhtmltopdf_path(self):
        paths = {
            "local": "/usr/local/bin/wkhtmltopdf",
            "staging": "/usr/bin/wkhtmltopdf",
            "production": "/usr/bin/wkhtmltopdf",
        }

        path = paths.get(self.app_env)

        if not path:
            raise ValueError(f"APP_ENV no válido: {self.app_env}")

        if not os.path.exists(path):
            raise FileNotFoundError(
                f"No se encontró wkhtmltopdf en la ruta configurada: {path}"
            )

        return path

    def _get_config(self):
        return pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)

    def _get_options(self):
        return {
            "encoding": "UTF-8",
            "page-size": "A4",
            "margin-top": "15mm",
            "margin-right": "10mm",
            "margin-bottom": "20mm",
            "margin-left": "10mm",
            "footer-font-size": "9",
            "footer-spacing": "5",
            "footer-left": self.footer_text,
            "footer-right": "Página [page] de [topage]",
            "enable-local-file-access": "",
        }

    def _render_html(self, context=None):
        if context is None:
            context = {}

        return render_to_string(self.template_html, context)

    def get_binary(self, context=None):
        html_string = self._render_html(context)

        pdf_binary = pdfkit.from_string(
            html_string,
            False,
            configuration=self._get_config(),
            options=self._get_options(),
        )

        return pdf_binary

    def save(self, filename, context=None, folder="pdfs"):
        html_string = self._render_html(context)

        folder_path = os.path.join(settings.MEDIA_ROOT, folder)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, filename)

        pdfkit.from_string(
            html_string,
            file_path,
            configuration=self._get_config(),
            options=self._get_options(),
        )

        return file_path
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)



def create_pdf_html(full_path, project_name_format, app_main):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "templates", "pdfs")
    file_path = os.path.join(folder_path, "test_pdf.html")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            color: #333;
            font-size: 14px;
            padding: 30px;
        }

        .container {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 30px;
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
        }

        .body {
            line-height: 1.7;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ title }}</h1>
        <div class="body">
            {{ body|linebreaks }}
        </div>
    </div>
</body>
</html>
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
