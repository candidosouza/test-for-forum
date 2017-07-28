from django import template

register = template.Library()


from city.models import SubSetor

@register.simple_tag
def get_sub_setor(setor):
    sub_setor = SubSetor.objects.filter(setor=setor)
    if sub_setor:
        return sub_setor
    return None
