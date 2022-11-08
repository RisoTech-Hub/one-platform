from django.forms import CharField as BaseCharField
from django.forms import ChoiceField as BaseChoiceField
from django.forms import ImageField as BaseImageField

from one.components.widgets import BootstrapInput, FloatingLabelSelectTwo, ImageInput


class CharField(BaseCharField):
    widget = BootstrapInput


class FloatingLabelCharField(BaseCharField):
    widget = BootstrapInput


class ImageField(BaseImageField):
    widget = ImageInput


class FloatingLabelChoiceField(BaseChoiceField):
    widget = FloatingLabelSelectTwo
