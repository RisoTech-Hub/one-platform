from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AllauthExtendConfig(AppConfig):
    name = "one.allauth_extend"
    verbose_name = _("Allauth Extend")

    def ready(self):
        pass
