from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ClientModel(BaseModel):
    session_id = models.CharField(null=False, max_length=255)
    remote_address = models.CharField(null=True, blank=True, max_length=255)
    user_agent = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self): 
         return self.session_id