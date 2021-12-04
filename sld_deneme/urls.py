from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("home.urls", namespace='home')),
    path('sld/', include("sld.urls", namespace='sld')),
    path('user/', include("user.urls", namespace='user')),
    path('admin/', admin.site.urls),
]
