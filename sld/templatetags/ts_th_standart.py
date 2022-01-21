from django import template

register = template.Library()


@register.filter  # gecis genisligi --> (kanat_genisligi) - 84
def gecis_genisligi_hesaplama(gecis_genisligi):
    return kanat_genisligi_hesaplama(gecis_genisligi) - 84


@register.filter  # kanat genisligi --> (gecis_genisligi + 42) / 2
def kanat_genisligi_hesaplama(gecis_genisligi):
    return round((gecis_genisligi + 42) / 2)


@register.filter  # etek olcusu --> (kanat_genisligi) - 48
def etek_olcusu(gecis_genisligi):
    return kanat_genisligi_hesaplama(gecis_genisligi) - 48
