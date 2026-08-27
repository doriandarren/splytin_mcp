import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_test_mail(full_path):
    create_class_test_mail(full_path)
    create_view_test_mail(full_path)
    



def create_class_test_mail(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Mail", "Test")
    file_path = os.path.join(folder_path, "TestMail.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<?php

namespace App\\Mail\\Test;

use Illuminate\\Bus\\Queueable;
use Illuminate\\Contracts\\Queue\\ShouldQueue;
use Illuminate\\Mail\\Mailable;
use Illuminate\\Mail\\Mailables\\Content;
use Illuminate\\Mail\\Mailables\\Envelope;
use Illuminate\\Queue\\SerializesModels;

class TestMail extends Mailable
{{
    use Queueable, SerializesModels;


    protected String $mySubject;
    protected String $myBody;


    /**
     * Create a new message instance
     */
    public function __construct($mySubject = 'Default Subject', $myBody = '')
    {{
        $this->mySubject = $mySubject;
        $this->myBody = $myBody;
    }}


    /**
     * Get the message envelope.
     */
    public function envelope(): Envelope
    {{
        return new Envelope(
            subject: $this->mySubject,
        );
    }}

    /**
     * Get the message content definition.
     */
    public function content(): Content
    {{
        return new Content(
            view: 'mails.test.test_mail',
            with: [
                'mySubject' => $this->mySubject,
                'myBody' => $this->myBody,
            ],
        );
    }}

    /**
     * Get the attachments for the message.
     *
     * @return array<int, \\Illuminate\\Mail\\Mailables\\Attachment>
     */
    public function attachments(): array
    {{
        return [];
    }}
}}

"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        


def create_view_test_mail(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "resources", "views", "mails", "test")
    file_path = os.path.join(folder_path, "test_mail.blade.php")

    os.makedirs(folder_path, exist_ok=True)

    content = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DeliveryNote</title>
    <style>
        /* Incluir Tailwind CSS como estilos en línea o utilizando un compilador de CSS */
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 1rem;
            font-family: Arial, sans-serif;
        }}

        .header {{
            background-color: #4A90E2;
            color: white;
            padding: 1px;
            text-align: center;
        }}

        .content {{
            background-color: #f9f9f9;
            padding: 1rem;
        }}

        .footer {{
            text-align: center;
            padding: 1rem;
            font-size: 0.875rem;
            color: #888;
        }}

        .button {{
            background-color: #4A90E2;
            color: white;
            padding: 0.5rem 1rem;
            text-decoration: none;
            border-radius: 0.25rem;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 3rem;
        }}

        th,
        td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}

        th {{
            background-color: #f2f2f2;
            text-align: left;
        }}

        p {{
            margin-bottom: 2rem;
            font-size: 1rem;
        }}
    </style>
</head>

<body>
    <div class="container">
        <div class="header">
            <h1>{{{{ $mySubject ?? '' }}}}</h1>
        </div>
        <div class="content">
            <p>Hola!</p>
            <p>
                Esto es un correo de Prueba.
            </p>
            <p>
                {{{{ $myBody ?? '' }}}}
            </p>

        </div>
        <div class="footer">

            <p style="font-size: 10px; text-align: justify;">
                <strong>AVISO LEGAL:</strong> Este mensaje y sus posibles documentos adjuntos son confidenciales y están
                dirigidos exclusivamente a sus destinatarios. Por favor, si Ud. no es uno de ellos, notifíquenoslo y
                elimine el mensaje de su sistema. De conformidad con la legislación vigente, queda prohibida la copia,
                difusión o revelación de su contenido a terceros sin el previo consentimiento por escrito de Portuarios.
                Asimismo, en relación con la normativa de protección de datos puede ejercer sus derechos de acceso,
                rectificación, cancelación, oposición y portabilidad de acuerdo a lo establecido en nuestra política
                de privacidad en la siguiente dirección: Calle Pablo Iglesias, 65. Hospitalet de Llobregat. 08908
                Barcelona, España.
            </p>

            <p style="font-size: 10px; text-align: justify;">
                <strong>LEGAL NOTICE:</strong> This message (including any attachments) may contain privileged and/or
                confidential information. Therefore, we would like to inform whoever may receive it by mistake that the
                information contained herein is strictly confidential, and its unauthorized use is prohibited by law.
                Therefore, in this case, please notify us by email and refrain from copying the message or forwarding
                it to third parties, and proceed to delete it immediately. According to the Organic Law of Protection of
                Personal Data, Portuarios informs you that your data is protected according to Organic Law 15/1999.
                The owner of the data will have, at any time, the right to access the files, and can also exercise
                the rights of rectification, cancellation and opposition in the terms included in the data protection
                legislation at the following address: Calle Pablo Iglesias, 65. Hospitalet de Llobregat. 08908
                Barcelona, Spain.
            </p>

            <hr style="margin: 1.5rem 0; border: none; border-top: 1px solid #ccc;">

            <p style="font-size: 12px;">&copy; {{{{ date('Y') }}}} Portuarios. All rights reserved.</p>

        </div>
    </div>

    @php
        //dd("OK");
    @endphp
</body>

</html>
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

