from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DynamicConfig(AppConfig):
    name = "one.core.dynamic"
    verbose_name = _("Dynamic")

    def ready(self):
        try:
            import one.core.dynamic.signals  # noqa F401
        except ImportError:
            pass
