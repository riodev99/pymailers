import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Environment, FileSystemLoader
import logging

class PyMailer:
    def __init__(self, config):
        self.smtp_host = config['smtp_host']
        self.smtp_port = config['smtp_port']
        self.email = config['email']
        self.password = config['password']
        self.to = config['to']
        self.subject = config['subject']
        self.body = config['body']
        self.display = config['display']
        self.attachments = config.get('attachments', [])
        self.template_path = config.get('template_path', '')
        self.template_context = config.get('template_context', {})

    def send(self):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.to
        msg['Subject'] = self.subject

        # Use Jinja2 to parse HTML template if provided
        if self.template_path:
            env = Environment(loader=FileSystemLoader(os.path.dirname(self.template_path)))
            template = env.get_template(os.path.basename(self.template_path))
            self.body = template.render(self.template_context)

        msg.attach(MIMEText(self.body, 'html'))

        # Attach files
        for file_path in self.attachments:
            part = MIMEBase('application', 'octet-stream')
            with open(file_path, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
            msg.attach(part)

        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
                smtp.starttls()
                smtp.login(self.email, self.password)
                smtp.send_message(msg)
                if self.display:
                    print(f"Email sent successfully to {self.to}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            sys.exit()

# Set up logging
logging.basicConfig(filename='pymailer.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Example usage
config = {
    'smtp_host': 'smtp.example.com',
    'smtp_port': 587,
    'email': 'your-email@example.com',
    'password': 'yourpassword',
    'to': 'recipient@example.com',
    'subject': 'Test Email',
    'body': 'This is a test email with an attachment.',
    'display': True,
    'attachments': ['/path/to/attachment1.pdf', '/path/to/attachment2.jpg'],
    'template_path': '/path/to/template.html',
    'template_context': {'username': 'John Doe'}
}

mailer = PyMailer(config)
mailer.send()
