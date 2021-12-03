from django.urls import path
from . import views


app_name = 'sld'
urlpatterns = [
    path('goruntule/<id>', views.isEmri_goruntule, name='isEmri_goruntule'),
    path('olustur', views.isEmri_olustur, name='isEmri_olustur'),
    path('liste', views.isEmri_listele, name='isEmri_listele'),
    path('pdf/', views.pdf_olustur, name='pdf_olustur'),
    path('gonder/', views.mail_gonder, name='mail_gonder'),
    path('home/', views.sld_home, name='sld_home')
]
