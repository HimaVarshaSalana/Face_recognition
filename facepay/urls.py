from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/',views.about,name='app-about'),
    path('mobilepay/',views.mobilepay,name='mobilepay'),
    path('banktransfer/',views.banktransfer,name='banktransfer'),
    path('recharge/',views.recharge,name='recharge'),
    path('facedetect/',views.facedetect,name='facedetect'),
    path('payment/',views.payment,name='payment'),
    path('success/',views.success,name='success'),
    path('qqrcode/',views.qrcode,name='qrcode'),
]
