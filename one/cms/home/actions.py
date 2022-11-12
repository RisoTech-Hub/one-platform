from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def get_cms_home_add():
    return {
        "label": _("Create CMS Home"),
        "url": reverse_lazy("cmshome:cmshome-create"),
        "class": "primary",
        "icon": "duotune/arrows/arr075.svg",
    }


def get_cms_home_quick_add():
    return {
        "type": "modal",
        "label": _("Quick Create CMS Home"),
        "url": f"{reverse_lazy('cmshome:cmshome-create')}?popup=1",
        "class": "success",
        "icon": "duotune/arrows/arr075.svg",
        "attributes": "quick-add-button",
    }
