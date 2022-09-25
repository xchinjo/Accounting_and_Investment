import email
from email import message
from django.db import models

class AiModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
