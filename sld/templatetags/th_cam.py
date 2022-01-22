from django import template

register = template.Library()


@register.filter  # kanat genisligi --> (gecis_genisligi + 84)
def kanat_genisligi_hesaplama(gecis_genisligi):
    return round(gecis_genisligi + 60)
