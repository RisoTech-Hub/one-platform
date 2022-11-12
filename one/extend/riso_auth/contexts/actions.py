from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def get_core_group_add():
    return {
        "label": _("Create Group"),
        "url": reverse_lazy("auth:group-create"),
        "class": "primary",
        "icon": "duotune/arrows/arr075.svg",
    }


def get_core_group_quick_add():
    return {
        "type": "modal",
        "label": _("Quick Create Group"),
        "url": f"{reverse_lazy('auth:group-create')}?popup=1",
        "class": "success",
        "icon": "duotune/arrows/arr075.svg",
        "attributes": "quick-add-button",
    }
