from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "one.users"
    verbose_name = _("User")

    def ready(self):
        try:
            import one.users.signals  # noqa F401
        except ImportError:
            pass
