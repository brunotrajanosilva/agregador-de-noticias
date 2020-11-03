from django import template

register = template.Library()

@register.filter(name="get_logo")
def get_logo(dictionary, key):
    return dictionary.get(key)