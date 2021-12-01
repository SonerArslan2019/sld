from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('/', home.urls),
    path('admin/', admin.site.urls),
    path('sld/', include("sld.urls", namespace='sld'))
]
