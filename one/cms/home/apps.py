from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "one.cms.home"
    verbose_name = _("Homes")

    def ready(self):
        try:
            import one.cms.home.signals  # noqa F401
        except ImportError:
            pass
