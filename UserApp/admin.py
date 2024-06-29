from django.contrib import admin
from . models import reg_tbl,Cart_tbl,Pay_tbl,Trans_tbl,Auction,Bid_tbl
# Register your models here.
admin.site.register(reg_tbl),
admin.site.register(Cart_tbl),
admin.site.register(Pay_tbl),
admin.site.register(Trans_tbl),
admin.site.register(Auction),
admin.site.register(Bid_tbl),