from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GroupsConfig(AppConfig):
    name = "one.groups"
    verbose_name = _("Groups")

    def ready(self):
        try:
            import one.groups.signals  # noqa F401
        except ImportError:
            pass
