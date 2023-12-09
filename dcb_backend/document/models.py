
from django.db import models
import os
from django.contrib.auth.models import User
from DCB_Backend import settings
from core.models import BaseModel
from django.dispatch import receiver

class DocumentModel(BaseModel):
    uploaded_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) # change null to false
    file = models.FileField(upload_to=settings.UPLOADPATH)
    name = models.CharField(null=False, max_length=255)
    vector_document_name = models.CharField(null=False, max_length=255)

    def __str__(self): 
         return self.name

@receiver(models.signals.post_delete, sender=DocumentModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `DocumentModel` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
