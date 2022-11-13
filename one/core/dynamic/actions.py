from django.utils.translation import gettext_lazy as _


def get_core_dynamic_field_schema_drawer():
    return {
        "type": "drawer",
        "label": _("Dynamic Field Config"),
        "url": "kt_fieldschemas_toggle",
        "class": "danger",
        "icon": "duotune/general/gen019.svg",
    }
