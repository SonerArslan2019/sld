from django.urls import path
from . import views


app_name = 'sld'
urlpatterns = [
    path('goruntule/', views.detail_view, name='detail'),
    path('olustur', views.create_view, name='create'),
    path('liste', views.list_view, name='list'),
    path('pdf/', views.make_pdf, name='make_pdf'),
    path('gonder/', views.send_mail, name='send_mail'),
    path('home/', views.home, name='home')
]
