from django import template

register = template.Library()


@register.filter  # gecis genisligi --> (toplam_genislik) - 126
def gecis_genisligi_hesaplama(toplam_genislik):
    return kanat_genisligi_hesaplama(toplam_genislik) - 126


@register.filter  # kanat genisligi --> (toplam_genislik + 84) / 3
def kanat_genisligi_hesaplama(toplam_genislik):
    return round((toplam_genislik + 84) / 3)


@register.filter  # etek olcusu --> (kanat_genisligi) - 48
def etek_olcusu(toplam_genislik):
    return kanat_genisligi_hesaplama(toplam_genislik) - 48
