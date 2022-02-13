from django import template

register = template.Library()


@register.filter(name="add_node")
def add_node(value, arg):
    """return value and previous arg"""
    return value, arg
