from django.db import models
from ProApp.models import comp_det
from django.utils import timezone


# Create your models here.
class reg_tbl(models.Model):
    fnm = models.CharField(max_length=25)
    mob = models.IntegerField()
    eml = models.EmailField()
    psw = models.CharField(max_length=25)
    cpsw = models.CharField(max_length=25)
   
class Cart_tbl(models.Model):
    customer = models.ForeignKey(reg_tbl,on_delete=models.CASCADE)
    product = models.ForeignKey(comp_det,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

class Pay_tbl(models.Model):
    pro = models.CharField(max_length=25)
    qty = models.IntegerField()
    prc = models.IntegerField()
    tot = models.IntegerField()
    fn = models.CharField(max_length=25)
    cd = models.IntegerField()
    ex = models.CharField(max_length=25)
    cvv = models.CharField(max_length=25)

class Trans_tbl(models.Model):
    fnm = models.CharField(max_length=25)
    vnm = models.CharField(max_length=25)
    dnm = models.CharField(max_length=25)
    address = models.TextField()
    bd = models.DateField()
    dd = models.DateField()
    sc = models.IntegerField()

class Auction(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    seller = models.CharField(max_length=25)
    goods_name = models.CharField(max_length=100)
    goods_description = models.TextField()
    goods_image = models.ImageField(upload_to='goods_images/')
    basic = models.IntegerField()
    ended = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the instance is being created
            self.start_time = timezone.now()  # Set start_time to current time if not already set
            if self.end_time is None:
                # Assuming end_time is one day after start_time, you can adjust this according to your requirements
                self.end_time = self.start_time + timezone.timedelta(days=1)
        super().save(*args, **kwargs)

    def auction_end(self):
        if self.end_time is not None and self.end_time <= timezone.now():
            self.ended = True
        else:
            self.ended = False
        self.save()
        super().save()

class Bid_tbl(models.Model):
    seller = models.CharField(max_length=25)
    gname = models.CharField(max_length=50)
    basic = models.IntegerField()
    st = models.CharField(max_length=25)
    et = models.CharField(max_length=25)
    bidder = models.CharField(max_length=25)
    mb = models.CharField(max_length=25)

