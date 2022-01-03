from django.apps import AppConfig


class EmailsConfig(AppConfig):
    """
    AppConfig of emails module
    """

    name = "one.emails"
    verbose_name = "Emails"

    def ready(self):
        pass
