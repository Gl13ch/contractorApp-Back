from django.db import models

# Create your models here.
class ToDo(models.Model):
    checked = models.BooleanField(default=False)
    detail = models.CharField(max_length=255)