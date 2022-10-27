from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MetronicConfig(AppConfig):
    name = "one.extend.metronic"
    verbose_name = _("Metronic Theme")

    def ready(self):
        pass
