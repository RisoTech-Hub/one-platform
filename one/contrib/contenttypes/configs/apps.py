from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConfigAppConfig(AppConfig):
    name = "one.contrib.contenttypes.configs"
    verbose_name = _("Content Type Configs")

    def ready(self):
        from .signals import create_or_update_contenttype_config  # noqa
