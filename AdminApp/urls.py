from django.urls import path
from . import views

urlpatterns=[

    path('Adminhome',views.Adminhome),
    path('userview',views.userview),
    path('edit',views.edit),
    path('update',views.update),
    path('delete',views.delete),
    path('driverview',views.driverview),
    path('driveredit',views.driveredit),
    path('driverupdate',views.driverupdate),
    path('driverdelete',views.driverdelete),
    path('vehicleview',views.vehicleview),
    path('vehicleedit',views.vehicleedit),
    path('vehicleupdate',views.vehicleupdate),
    path('vehicledelete',views.vehicledelete),
    path('Auction_view',views.Auction_view),
    path('auction_end',views.auction_end),
    path('adminbid_view',views.adminbid_view),
    path('adminbid_result',views.adminbid_result),
]