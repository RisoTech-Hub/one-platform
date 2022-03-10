from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SettingsConfig(AppConfig):
    """
    AppConfig of settings module
    """

    name = "one.settings"
    verbose_name = _("Settings")

    def ready(self):
        pass
