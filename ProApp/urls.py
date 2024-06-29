from django.urls import path
from . import views

urlpatterns=[
    path('comphome',views.comphome),
    path('compreg',views.compreg),
    path('proddetails',views.proddetails),
    path('cartdelete',views.cartdelete),
]