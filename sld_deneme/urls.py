from django.contrib import admin
from django.urls import path, include
from sld import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.giris_sayfasi, name='giris_sayfasi'),
    path('sld/', include("sld.urls", namespace='sld'))
]
