from django import template

register = template.Library()

@register.filter
def split_promise(value):
    result = value.replace('/', "<br>")
    return result