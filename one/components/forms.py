from django.forms import CharField as BaseCharField
from django.forms import ImageField as BaseImageField

from one.components.widgets import BootstrapInput, ImageInput


class CharField(BaseCharField):
    widget = BootstrapInput


class ImageField(BaseImageField):
    widget = ImageInput
