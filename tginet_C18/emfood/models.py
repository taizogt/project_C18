from django.db import models
from django.conf import settings
# Create your models here.

class Emfood(models.Model):
    name = models.CharField(max_length=200)
    num = models.IntegerField()
    expire_date = models.DateTimeField(blank=True, null=True)