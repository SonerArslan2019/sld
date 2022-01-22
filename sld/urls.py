from django.urls import path
from . import views

app_name = 'sld'
urlpatterns = [
    path('goruntule/<id>', views.isemri_goruntule, name='isEmri_goruntule'),
    path('olustur', views.isemri_olustur, name='isEmri_olustur'),
    path('liste', views.isemri_listele, name='isEmri_listele'),
    path('pdf/', views.pdf_olustur, name='pdf_olustur'),
    path('gonder/', views.mail_gonder, name='mail_gonder'),
]
