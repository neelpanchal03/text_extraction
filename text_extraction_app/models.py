from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    extracted_text = models.TextField()
    email = models.EmailField()
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} - {self.created_at}'

    class Meta:
        db_table = 'documents'
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
