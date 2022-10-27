from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AllauthExtendConfig(AppConfig):
    name = "one.extend.riso_allauth"
    verbose_name = _("Allauth Extend")

    def ready(self):
        pass
