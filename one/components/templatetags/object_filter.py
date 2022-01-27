from django import template
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.filter(name="obj_val")
def object_value(value, arg):
    """return value of object in arg"""
    if value not in ["", None]:
        _value = getattr(arg, value)
        return _(_value) if isinstance(_value, str) else _value
    return ""


@register.filter(name="obj_type")
def object_type(obj):
    """Type of object"""
    return type(obj)


@register.filter(name="obj_meta")
def object_meta(obj):
    """Meta of object"""
    return obj.__dict__
