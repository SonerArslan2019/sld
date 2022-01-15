from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include("home.urls", namespace='home')),
                  path('sld/', include("sld.urls", namespace='sld')),
                  path('user/', include("user.urls", namespace='user')),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
