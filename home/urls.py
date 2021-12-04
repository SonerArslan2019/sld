from django.urls import path

from .views import *

app_name = "home"

urlpatterns = [
    path('', giris_sayfasi, name='giris_sayfasi'),
    path('genel_kapilar/', genel_kapilar, name='genel_kapilar'),
    path('sld_kapilar/', sld_kapilar, name='sld_kapilar'),
    path('401/', hata_401, name='hata_401'),
]
