from django.db import models
from django.conf import settings
# Create your models here.

class Emfood(models.Model):
    name = models.CharField(max_length=200)
    num = models.IntegerField()
    # 時刻あり期限
    expire_date = models.DateTimeField(blank=True, null=True)
    user=models.CharField(max_length=10, default="unknown")
    # 時刻なし消費期限
    limit_date=models.DateField(blank=True, null=True )