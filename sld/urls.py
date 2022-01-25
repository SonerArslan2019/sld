from django.urls import path
from . import views

app_name = 'sld'
urlpatterns = [
    path('goruntule/<int:id>', views.isemri_goruntule, name='goruntule'),
    path('olustur', views.isemri_olustur, name='olustur'),
    path('liste', views.isemri_listele, name='listele'),
    path('pdf/', views.pdf_olustur, name='pdf'),
    path('gonder/', views.mail_gonder, name='mail'),
]
