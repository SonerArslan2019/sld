from django import template

register = template.Library()


@register.filter  # kanat genisligi --> (toplam_genislik + 168) / 4
def kanat_genisligi_hesaplama(toplam_genislik):
    return round((toplam_genislik + 168) / 4)
