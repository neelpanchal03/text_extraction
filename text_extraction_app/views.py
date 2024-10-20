from django.shortcuts import render, redirect
from .models import Document
from .tasks import extract_text_async
from asgiref.sync import sync_to_async


async def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        email = request.POST.get('email')

        if not file or not email:
            return render(request, 'upload_file.html', {
                'error': 'Both email and file are required.'
            })

        if file:
            # Check if the file is a supported format
            valid_extensions = ['pdf', 'doc', 'docx']
            valid_content_types = ['application/pdf',
                                   'application/msword',
                                   'application/vnd.openxmlformats-officedocument.wordprocessingml.document']

            file_extension = file.name.split('.')[-1].lower()
            if file_extension not in valid_extensions or file.content_type not in valid_content_types:
                return render(request, 'upload_file.html', {
                    'error': 'Unsupported file type. Please upload a PDF, DOC, or DOCX file.'
                })

            # Create the document object in the database and trigger Celery task
            doc = await sync_to_async(Document.objects.create)(file=file, email=email)
            extract_text_async.delay(doc.id)

            return render(request, 'upload_file.html', {
                'success': 'Your file has been uploaded successfully and is being processed!'
            })

    return render(request, 'upload_file.html')
