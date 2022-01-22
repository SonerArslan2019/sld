from django import template

register = template.Library()


@register.filter  # gecis genisligi --> (kanat_genisligi) - 84
def gecis_genisligi_hesaplama(toplam_genislik):
    return kanat_genisligi_hesaplama(toplam_genislik) - 72


@register.filter  # kanat genisligi --> (toplam_genislik + 30) / 2
def kanat_genisligi_hesaplama(toplam_genislik):
    return round((toplam_genislik + 30) / 2)


@register.filter  # etek olcusu --> (gecis_genisligi) - 30
def etek_olcusu(gecis_genisligi):
    return kanat_genisligi_hesaplama(gecis_genisligi) - 30
