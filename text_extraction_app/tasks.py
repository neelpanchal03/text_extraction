import os

from celery import shared_task
from django.core.mail import send_mail
from .models import Document
from .utils import extract_text_from_pdf, extract_text_from_docx, extract_text_from_doc


@shared_task
def extract_text_async(doc_id):
    try:
        doc = Document.objects.get(id=doc_id)
        if doc.file:
            file_path = doc.file.path

        if file_path.endswith('.pdf'):
            doc.extracted_text = extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            doc.extracted_text = extract_text_from_docx(file_path)
        elif file_path.endswith('.doc'):
            doc.extracted_text = extract_text_from_doc(file_path)

        doc.processed = True
        doc.save()
        send_email_notification(doc)

    except Document.DoesNotExist:
        pass


def send_email_notification(doc):
    email_from = os.getenv('EMAIL_HOST_USER')
    send_mail(
        subject='Your Document Text Extraction is Complete',
        message=f'Hello, your text extraction is complete. Extracted text: {doc.extracted_text}',
        from_email=email_from,
        recipient_list=[doc.email],
    )