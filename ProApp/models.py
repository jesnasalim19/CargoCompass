from django.db import models

# Create your models here.
class comp_log(models.Model):
    cnm = models.CharField(max_length=25)
    usr = models.CharField(max_length=25)
    psw = models.CharField(max_length=25)
    def __str__(self):
        return self.usr

class comp_det(models.Model):
    cnm = models.CharField(max_length=25)
    cat = models.CharField(max_length=25)
    pro = models.CharField(max_length=25)
    pic = models.FileField(upload_to='pictures')
    prc = models.IntegerField()
    des = models.TextField()
   