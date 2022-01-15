from django import forms
from django.forms import widgets

from .models import SldModel


class SldForm(forms.ModelForm):
    class Meta:
        model = SldModel
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
            'toplam_genislik',
            'ustluk',
            'toplam_yukseklik',
            'mekanizma_genisligi',
            'opsiyonlar',
            'radar_aktivasyonlar',
        ]

