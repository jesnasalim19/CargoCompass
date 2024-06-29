from django.db import models

# Create your models here.
class adminlog(models.Model):
    eml = models.EmailField()
    psw = models.CharField(max_length=10)