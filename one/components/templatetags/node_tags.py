from django import template

register = template.Library()


@register.filter(name="add_node")
def add_node(value, arg):
    """return string with dot"""
    return value, arg
