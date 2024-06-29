from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('reg',views.reg),
    path('log',views.log),
    path('home',views.home),
    path('cat',views.cat),
    path('prod',views.prod),
    path('addtocart',views.addtocart),
    path('viewcart',views.viewcart),
    path('paydirect',views.paydirect),
    path('pay',views.pay),
    path('transport',views.transport),
    path('Auction_details',views.Auction_details),
    path('bid_submit',views.bid_submit),
    path('bid_max',views.bid_max),
    path('bid_result',views.bid_result),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)