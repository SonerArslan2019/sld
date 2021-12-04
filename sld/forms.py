from django import forms

from .models import SldModel


class SldForm(forms.ModelForm):
    class Meta:
        model = SldModel
        # fields = "__all__"
        fields = [
            'user',
            'crm',
            'firma_bilgileri',
            'teslim_tarihi',
            'cam',
            'bitis',
            'kapi_tipi',
            'acilis_yonu',
            'gecis_genisligi',
            'gecis_yuksekligi',
            'ustluk',
            'toplam_yukseklik',
            'mekanizma_genisligi',
        ]
