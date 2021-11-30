from django.contrib import admin

from .models import SldModel

admin.site.register(SldModel)


class SldAdmin(admin.ModelAdmin):
    search_fields = ("firma_bilgileri", "crm", "kapi_tipi")
    list_display = (
        'hazirlayan', 'teslim_tarihi', 'olusturma_tarihi'
    )


admin.site.site_header = "ARSLAN YAPI (Imalat) YONETIM PANELI"
