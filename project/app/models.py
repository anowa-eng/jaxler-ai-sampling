from django.db import models

# Create your models here.
class ConversationalData(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    class Meta:
        verbose_name_plural = 'Conversational data'