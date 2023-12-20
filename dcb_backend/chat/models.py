from django.db import models

from core.models import BaseModel, ClientModel


class ChatModel(BaseModel):
    question = models.CharField(max_length=2000, null=False, blank=False)
    response = models.CharField(max_length=2000)
    new_conversation = models.BooleanField()
    client = models.ForeignKey(ClientModel, on_delete=models.SET_NULL, null=True)

    def __str__(self): 
         return f"{self.client}@{self.created}"
