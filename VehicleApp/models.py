from django.db import models

# Create your models here.
class Vehicle_tbl(models.Model):
    vnm = models.CharField(max_length=25)
    vno = models.CharField(max_length=25)
    dnm = models.CharField(max_length=25)
    dim = models.FileField(upload_to='dpic')
    lcn = models.FileField(upload_to='License')
    lno = models.CharField(max_length=25)
    loc = models.CharField(max_length=25)
    mob = models.IntegerField()
    add = models.TextField()