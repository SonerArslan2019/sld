from django.contrib import admin
from django.urls import path, include
from sld import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ana_sayfa, name='ana_sayfa'),
    path('sld/', include("sld.urls", namespace='sld'))
]
