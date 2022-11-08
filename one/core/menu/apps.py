from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MenusConfig(AppConfig):
    name = "one.core.menu"
    verbose_name = _("Menus")

    def ready(self):
        try:
            import one.core.menu.signals  # noqa F401
        except ImportError:
            pass
