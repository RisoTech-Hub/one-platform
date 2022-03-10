from django import template
from django.utils.translation import gettext_lazy as _

from one.components.utils import eval_expression

register = template.Library()


@register.filter(name="obj_val")
def object_value(value, arg):
    """return value of object in arg"""
    # In case get value from dict
    if isinstance(arg, dict) and value in arg:
        return arg[value]
    # In case value is tuple for nested object
    if isinstance(value, tuple):
        try:
            data = eval_expression(f"arg.{value[1]}.get_{value[0]}_html")
        except AttributeError:
            data = eval_expression(f"arg.{value[1]}.get_{value[0]}_display()")
        return data
    # In case get value in object
    if value not in ["", None] and hasattr(arg, value):
        try:
            data = eval_expression(f"arg.get_{value}_html")
        except AttributeError:
            _value = getattr(arg, value)
            data = _(_value) if isinstance(_value, str) else _value
        return data
    return ""


@register.filter(name="obj_type")
def object_type(obj):
    """Type of object"""
    return type(obj)


@register.filter(name="obj_meta")
def object_meta(obj):
    """Meta of object"""
    return obj.__dict__
