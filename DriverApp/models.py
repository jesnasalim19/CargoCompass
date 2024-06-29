from django.db import models

# Create your models here.
class Driver_tbl(models.Model):
    dnm = models.CharField(max_length=25)
    dim = models.FileField(upload_to='dpic')
    lno = models.CharField(max_length=15)
    lcn = models.FileField(upload_to='license')
    loc = models.CharField(max_length=25)
    mob = models.IntegerField()
    add = models.TextField()