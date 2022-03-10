from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PagesConfig(AppConfig):
    """
    AppConfig of pages module
    """

    name = "one.pages"
    verbose_name = _("Page")

    def ready(self):
        pass
