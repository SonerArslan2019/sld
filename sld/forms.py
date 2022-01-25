from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms

from .models import SldModel


class SldForm(forms.ModelForm):
    class Meta:
        model = SldModel
        fields = [
            'crm',
            'firma_bilgileri',
            'sevk_adresi',
            'teslim_tarihi',
            'teslim_sekli',
            'paketleme_sekli',
            'cam',
            'bitis',
            'notlar',
            'kapi_tipi',
            'gecis_genisligi',
            'gecis_yuksekligi',
            'ustluk',
            'toplam_genislik',
            'toplam_yukseklik',
            'mekanizma_genisligi',
            'acilis_yonu',
            'opsiyonlar',
            'radar_aktivasyonlar',
        ]
        widgets = {
            'teslim_tarihi': DatePickerInput(format='%d/%m/%Y'),
        }
