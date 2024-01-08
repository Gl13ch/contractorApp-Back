from django.db import models
from users.models import User

# Create your models here.
class JobBoard(models.Model):
    image = models.FileField(upload_to=None)
    description = models.TextField()
    comments = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)