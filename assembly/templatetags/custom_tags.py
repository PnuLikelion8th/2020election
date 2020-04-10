from django import template

register = template.Library()

@register.filter
def split_promise(value):
    result = value.replace('/', "<br>flag").split('flag')
    real_result = ""
    for i in result:
        real_result += ("▶ " + str(i))
    return real_result