from django import forms

from .models import SldModel


class SldForm(forms.ModelForm):
    class Meta:
        model = SldModel
        fields = "__all__"
