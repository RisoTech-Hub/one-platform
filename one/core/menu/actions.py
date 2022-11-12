from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def get_core_menu_add():
    return {
        "label": _("Create Menu"),
        "url": reverse_lazy("menu:menu-create"),
        "class": "primary",
        "icon": "duotune/arrows/arr075.svg",
    }
