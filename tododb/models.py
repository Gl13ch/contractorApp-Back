from django.db import models

# Create your models here.
class Punchlist(models.Model):
    name_of_punchlist = models.CharField(max_length=100, unique=True, null=True, blank=True)

class Punch(models.Model):
    checked = models.BooleanField(default=False)
    detail = models.CharField(max_length=255)
    punchlist_list = models.ForeignKey(Punchlist, on_delete=models.CASCADE, null=True, blank=True)
