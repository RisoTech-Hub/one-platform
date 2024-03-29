from django.contrib.sites.models import Site

from one.components.fields import CharField, ImageField
from one.components.forms import ModelForm
from one.contrib.sites.settings.models import Setting


class SettingForm(ModelForm):
    favicon = ImageField(required=False)
    logo = ImageField(required=False)
    dark_logo = ImageField(required=False)
    small_logo = ImageField(required=False)
    mobile_logo = ImageField(required=False)

    class Meta:
        model = Setting
        exclude = ["site"]


class PopupSettingForm(ModelForm):
    class Meta:
        model = Setting
        exclude = ["site"]


class SiteForm(ModelForm):
    name = CharField()
    domain = CharField()

    class Meta:
        model = Site
        fields = ["name", "domain"]
