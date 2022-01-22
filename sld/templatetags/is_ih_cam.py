from django import template

register = template.Library()


@register.filter  # gecis genisligi --> (toplam genislik / 4 ) * 2 - 42
def gecis_genisligi_hesaplama(toplam_genislik):
    return round(toplam_genislik / 4) * 2 - 42


@register.filter  # kanat genisligi --> (gecis_genisligi + 68) / 4
def kanat_genisligi_hesaplama(toplam_genislik):
    return round((gecis_genisligi_hesaplama(toplam_genislik) + 68) / 4)
